# استبدل الجزء بتاع الـ return render_template_string في الكود عندك بده:

    return render_template_string('''
        <body style="background:#000; color:#fff; text-align:center; font-family:sans-serif; padding:20px;">
            <div style="border:2px solid #1db954; border-radius:20px; padding:20px; max-width:400px; margin:auto; background:#111; box-shadow: 0 0 20px #1db954;">
                <h1 style="color:#1db954;">🎸 محرك يوسف الموسيقي</h1>
                <form method="POST">
                    <input type="text" name="query" placeholder="اكتب اسم الأغنية هنا..." style="width:100%; padding:15px; border-radius:25px; border:none; margin-bottom:15px; text-align:center; background:#222; color:#fff;">
                    <button type="submit" style="width:100%; padding:12px; border-radius:25px; border:none; background:#1db954; color:#000; font-weight:bold; cursor:pointer;">تشغيل فوري</button>
                </form>
                
                {% if v_id %}
                    <div style="margin-top:20px; border-radius:15px; overflow:hidden; border:1px solid #333;">
                        <iframe width="100%" height="230" 
                                src="https://www.youtube-nocookie.com/embed/{{ v_id }}?autoplay=1&rel=0" 
                                frameborder="0" 
                                allow="autoplay; encrypted-media" 
                                allowfullscreen>
                        </iframe>
                    </div>
                {% endif %}
            </div>
            <p style="font-size:12px; color:#555; margin-top:20px;">🚀 تطوير يوسف - تالتة ثانوي</p>
        </body>
    ''', v_id=v_id)
