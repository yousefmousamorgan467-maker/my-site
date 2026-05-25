from flask import Flask, render_template, request, jsonify, send_file
import yt_dlp
import os
import tempfile
import uuid

app = Flask(__name__)

def search_and_extract(query):
    ydl_opts = {
        'format': 'bestaudio/best',
        'quiet': True,
        'no_warnings': True,
        'extract_flat': False,
        'skip_download': True,
        'noplaylist': True,
        'default_search': 'ytsearch5:',
        'source_address': '0.0.0.0',
    }
    results = []
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(query, download=False)
            entries = info.get('entries', [])
            for entry in entries:
                if entry is None:
                    continue
                audio_url = entry.get('url')
                webpage_url = entry.get('webpage_url')
                title = entry.get('title')
                duration = entry.get('duration')
                if duration:
                    mins, secs = divmod(duration, 60)
                    duration_str = f"{mins}:{secs:02d}"
                else:
                    duration_str = "غير معروف"
                results.append({
                    'title': title,
                    'duration': duration_str,
                    'webpage_url': webpage_url,
                    'audio_url': audio_url,
                })
        return results
    except Exception as e:
        print(f"خطأ في البحث: {e}")
        return []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    q = request.args.get('q', '')
    if not q:
        return jsonify([])
    results = search_and_extract(q)
    return jsonify(results)

@app.route('/download')
def download():
    url = request.args.get('url', '')
    if not url:
        return "لم يتم توفير رابط", 400
    tmp_dir = tempfile.gettempdir()
    outtmpl = os.path.join(tmp_dir, '%(title)s.%(ext)s')
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': outtmpl,
        'quiet': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'noplaylist': True,
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            final_file = ydl.prepare_filename(info).replace('.webm', '.mp3').replace('.m4a', '.mp3')
            base = os.path.splitext(final_file)[0]
            for ext in ['.mp3', '.webm', '.m4a', '.opus']:
                candidate = base + ext
                if os.path.exists(candidate):
                    final_file = candidate
                    break
            return send_file(final_file, as_attachment=True, download_name=info.get('title','audio')+'.mp3')
    except Exception as e:
        return f"خطأ في التحميل: {e}", 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
