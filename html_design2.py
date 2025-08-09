#!/usr/bin/env python3
"""
Kerala Floods 2018 Blog Generator
Embeds images as base64 data URIs into a single HTML file
"""
import base64
import os
from pathlib import Path

# --- EDIT: Add your image filenames here (must be in same folder as this script) ---
image_files = [
    "study-area.jpeg",
    "sentinel1-floodmaps.jpeg", 
    "figure9c.jpeg",
    "figure9a.jpeg",
    "figure10a.jpeg"
]

# Output filename
output_file = "kerala_floods_blog.html"

def encode_image_to_data_uri(path: Path) -> str:
    """Convert image file to base64 data URI"""
    ext = path.suffix.lower().lstrip('.')
    if ext in ('jpg', 'jpeg'):
        mime = 'image/jpeg'
    elif ext == 'png':
        mime = 'image/png'
    elif ext == 'gif':
        mime = 'image/gif'
    elif ext == 'webp':
        mime = 'image/webp'
    else:
        mime = 'application/octet-stream'
    
    try:
        data = path.read_bytes()
        b64 = base64.b64encode(data).decode('ascii')
        return f"data:{mime};base64,{b64}"
    except Exception as e:
        print(f"Error encoding {path}: {e}")
        return ""

def main():
    cwd = Path.cwd()
    print(f"Looking for images in: {cwd}")
    
    # Build data URIs for existing images
    data_uris = {}
    for filename in image_files:
        img_path = cwd / filename
        if img_path.exists():
            print(f"✓ Encoding {filename}...")
            data_uris[filename] = encode_image_to_data_uri(img_path)
        else:
            print(f"✗ Warning: {filename} not found - using placeholder")
            data_uris[filename] = ""

    # Generate the complete HTML
    html_content = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>Kerala Floods 2018 - Satellite Analysis</title>
<style>
body{{font-family:system-ui,-apple-system,Segoe UI,Roboto,Arial;margin:0;background:#f6f7f9;color:#111}}
.container{{max-width:1100px;margin:2rem auto;padding:1rem}}
.post{{background:#fff;padding:1.5rem;border-radius:10px;box-shadow:0 6px 20px rgba(16,24,40,0.06)}}
.hero img,.fig-img{{width:50%;height:50%;border-radius:6px;background:#eee}}
figure{{margin:1rem 0}}
figcaption{{font-size:.9rem;color:#6b7280;margin-top:0.5rem;font-style:italic}}
.grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:12px}}
.row{{display:flex;gap:12px;flex-wrap:wrap}}
.row img{{max-width:48%}}
.small{{font-size:.9rem;color:#6b7280}}
h1{{color:#1f2937;font-size:2.5rem;margin-bottom:0.5rem}}
.title-header{{background:linear-gradient(135deg,rgba(59,130,246,0.9),rgba(16,185,129,0.9)),url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 300"><path d="M0,200 Q300,160 600,180 T1200,200 L1200,300 L0,300 Z" fill="%23e0f2fe"/><path d="M0,220 Q300,180 600,200 T1200,220 L1200,300 L0,300 Z" fill="%23b3e5fc"/><path d="M0,240 Q300,200 600,220 T1200,240 L1200,300 L0,300 Z" fill="%2381d4fa"/></svg>');background-size:cover;background-position:center;color:white;padding:3rem 1.5rem;border-radius:12px;margin-bottom:2rem;text-align:center;position:relative;overflow:hidden}}
.title-header::before{{content:'';position:absolute;top:0;left:0;right:0;bottom:0;background:rgba(0,0,0,0.1);z-index:1}}
.title-header h1{{position:relative;z-index:2;color:white;margin:0;text-shadow:2px 2px 4px rgba(0,0,0,0.3)}}
.title-header .small{{position:relative;z-index:2;color:rgba(255,255,255,0.9);margin-top:0.5rem}}
h2{{color:#374151;font-size:1.8rem;margin-top:2rem;margin-bottom:1rem;border-bottom:2px solid #e5e7eb;padding-bottom:0.5rem}}
p{{line-height:1.6;margin-bottom:1rem;text-align:justify}}
.highlight{{background:linear-gradient(120deg, #fef3c7, #fcd34d);padding:0.2rem 0.4rem;border-radius:3px;font-weight:600}}
.stats{{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:1rem;margin:1.5rem 0;background:#f8fafc;padding:1rem;border-radius:8px}}
.stat-card{{text-align:center;padding:1rem}}
.stat-card:nth-child(1){{background:linear-gradient(135deg,#667eea,#764ba2);color:white;border-radius:8px}}
.stat-card:nth-child(2){{background:linear-gradient(135deg,#f093fb,#f5576c);color:white;border-radius:8px}}
.stat-card:nth-child(3){{background:linear-gradient(135deg,#4facfe,#00f2fe);color:white;border-radius:8px}}
.stat-card:nth-child(4){{background:linear-gradient(135deg,#43e97b,#38f9d7);color:#1f2937;border-radius:8px}}
.stat-card:nth-child(5){{background:linear-gradient(135deg,#fa709a,#fee140);color:#1f2937;border-radius:8px}}
.stat-number{{font-size:1.5rem;font-weight:bold;color:inherit}}
footer{{margin-top:1.5rem;padding-top:1rem;border-top:1px solid #e5e7eb}}
.placeholder{{width:100%;height:400px;display:flex;align-items:center;justify-content:center;color:white;font-size:1.2rem;border-radius:6px;font-weight:bold}}
</style>
</head>
<body>
<div class="container">
  <article class="post">
    <div class="title-header">
      <h1>How Satellite Data Analytics Helps Save Lives</h1>
        <p class="small"><em>Based on: Assessment of Kerala floods 2018</em></p>
    </div>
    
    <section>
      <h2>When Nature Unleashed Its Fury</h2>
      <p>Picture this: In just five days, Kerala received rainfall equivalent to what it normally gets in two and a half months. The monsoon of August 2018 didn't just bring rain—it brought devastation on an unprecedented scale. Rivers swelled beyond recognition, dams reached dangerous levels, and entire districts disappeared under murky floodwaters that stretched as far as the eye could see.</p>
      
      <p>As rescue helicopters circled overhead and boats navigated through submerged streets, a different kind of eye was watching from 700 kilometers above: satellites. While traditional monitoring systems failed and communication networks went dark, space-based sensors continued their silent vigil, capturing the unfolding disaster with remarkable precision.</p>
      
      <p>This is the story of how <span class="highlight">satellite technology</span> transformed our understanding of one of India's worst natural disasters, and more importantly, how it's revolutionizing the way we respond to floods worldwide. Our focus centers on the Alappuzha and Kottayam districts—a region where urban centers, vast wetlands, and the sprawling Vembanad Lake created a perfect storm of flooding complexity.</p>
      
      <p>What happened in Kerala wasn't just a local tragedy; it was a preview of our climate-changed future. But it also showcased how cutting-edge satellite analytics can turn the tide in disaster response—literally helping to save lives when every minute counts.</p>
    </section>

    <figure class="hero">
      {f'<img src="{data_uris.get("study-area.jpeg", "")}" alt="Study area map" class="fig-img"/>' if data_uris.get("study-area.jpeg") else '<div class="placeholder" style="background:linear-gradient(45deg,#3b82f6,#06b6d4)">Study Area Map - Alappuzha & Kottayam</div>'}
      <figcaption>Map showing Alappuuzha and Kottayam regions in Kerala, India.</figcaption>
    </figure>

    <section>
      <h2>Flood Devastation (Field Photos)</h2>
      <p>The 2018 Kerala floods unleashed unprecedented devastation across multiple districts, leaving behind scenes of 
      utter destruction and human suffering. In Padanad, severe soil erosion threatened homes perched on unstable hillsides,
      while Chengannur witnessed massive trees uprooted and scattered like matchsticks across the landscape. The residential
      streets of Kadapra and commercial areas of Thiruvalla were transformed into vast water bodies, with houses and
      buildings standing like isolated islands amidst the murky floodwaters.</p>
      
      <figure>
        {f'<img src="{data_uris.get("sentinel1-floodmaps.jpeg", "")}" alt="Field photos" class="fig-img"/>' if data_uris.get("sentinel1-floodmaps.jpeg") else '<div class="placeholder" style="background:linear-gradient(45deg,#ef4444,#f97316,#eab308,#22c55e)">Field Photos - Flood Devastation</div>'}
        <figcaption>a) Flood aftermath in Padanad, b) Flood damage in Chengannur, c) Flooded streets in Kadapra and 
        d) Inundation in Thiruvalla</figcaption>
      </figure>

      <p>These images capture the sheer scale of nature's fury that brought normal life to a complete standstill, forcing communities to navigate their
      submerged neighborhoods by boat and highlighting the vulnerability of human settlements against extreme weather events.</p>
    </section>

    <section>
      <h2>Why Real-Time Satellite Monitoring is a Game-Changer for Flood Response</h2>
      <p>When disaster strikes—like the devastating 2018 Kerala floods that submerged entire communities—every minute counts. Traditional flood monitoring methods often leave rescue teams flying blind, relying on patchy ground reports and outdated information when lives hang in the balance. This is where satellite technology becomes a literal lifesaver.</p>
      
      <p>Imagine having eyes in the sky that never blink. <span class="highlight">Synthetic Aperture Radar (SAR)</span> satellites do exactly that, cutting through storm clouds and darkness to map flooded areas in real-time. Unlike optical satellites that get blocked by cloudy skies (which, let's face it, are pretty common during floods!), SAR sensors use radar waves to "see" through weather conditions and provide crystal-clear images of water extent, even at 2 AM during a thunderstorm.</p>
      
      <p>But here's where it gets really exciting: modern analytics and AI can process this satellite data in near real-time, automatically detecting changes and generating flood maps within hours of data acquisition. Emergency responders can pinpoint exactly where people are trapped, which roads are still passable, and which areas need immediate attention—all from space-based observations.</p>
      
      <p>The result? Instead of sending rescue boats on guesswork missions, teams can strategically deploy resources where they're needed most. It's the difference between reactive scrambling and proactive, data-driven disaster response.</p>
      
      <p>To demonstrate the power of this approach, we analyzed SAR satellite data from the 2018 Kerala floods, creating detailed flood extent maps and conducting impact assessments for the affected regions. Our analysis reveals how satellite-based monitoring could have transformed the emergency response during this catastrophic event. Let's dive into the results and see exactly how this technology works in practice.</p>
    </section>

    <section>
    <h2>Results: Mapping Floods from Space</h2>
    <p>Our analysis leveraged a comprehensive satellite dataset to reconstruct the flooding timeline and assess its devastating impact across Kerala. We utilized <span class="highlight">C-band Sentinel-1</span> time series data for continuous monitoring capabilities, complemented by <span class="highlight">L-band ALOS-2/PALSAR-2</span> observations that provided superior penetration through dense vegetation—a crucial advantage in Kerala's tropical landscape.</p>

    <div class="stats">
        <div class="stat-card">
            <div class="stat-number">Above 400 km²</div>
            <div>Flooded Area Detected</div>
        </div>
        <div class="stat-card">
            <div class="stat-number">90%</div>
            <div>Overall Detection Accuracy</div>
        </div>
        <div class="stat-card">
            <div class="stat-number">81.6%</div>
            <div>Critical Success Index</div>
        </div>
        <div class="stat-card">
            <div class="stat-number">6 days</div>
            <div>Sentinel-1 Revisit Cycle</div>
        </div>
    </div>


      <p>The multi-frequency SAR approach proved highly effective in capturing the flood dynamics. Sentinel-1's frequent revisit cycle (every 6 days) allowed us to track the rapid progression of flooding from August 15-19, 2018, when the disaster reached its peak. The C-band data excelled at detecting open water surfaces and urban flooding, while the L-band PALSAR-2 data was instrumental in identifying inundation beneath the dense coconut groves and banana plantations that characterize much of Kerala's terrain.</p>

      <figure>
        {f'<img src="{data_uris.get("figure9c.jpeg", "")}" alt="Sentinel-1 maps" class="fig-img"/>' if data_uris.get("figure9c.jpeg") else '<div class="placeholder" style="background:linear-gradient(45deg,#8b5cf6,#06b6d4,#10b981)">Sentinel-1 RGB Analysis Maps</div>'}
        <figcaption>RGB-based area (satellite modelled area) shows inundation modelled before, during and after the flood event.</figcaption>
      </figure>

      <p>Our automated flood detection algorithm identified over 400 square kilometers of inundated area at peak flooding—a staggering 
      extent that encompassed agricultural lands, urban centers, and critical infrastructure. The time series analysis revealed that flooding persisted for nearly two weeks in low-lying areas, with some regions remaining waterlogged well into September.</p>

      <figure>
        {f'<img src="{data_uris.get("figure9a.jpeg", "")}" alt="Occurrence map" class="fig-img"/>' if data_uris.get("figure9a.jpeg") else '<div class="placeholder" style="background:linear-gradient(45deg,#ef4444,#22c55e,#3b82f6)">Flood Occurrence Map</div>'}
        <figcaption>Change Map (Occurrence): Red for August 9, Green for August 21, Blue for August 27</figcaption>
      </figure>

      <figure>
        {f'<img src="{data_uris.get("figure10a.jpeg", "")}" alt="Recession map" class="fig-img"/>' if data_uris.get("figure10a.jpeg") else '<div class="placeholder" style="background:linear-gradient(45deg,#ef4444,#22c55e,#3b82f6)">Flood Recession Map</div>'}
        <figcaption>Change Map (Recession): Red for August 21, Green for August 27, Blue for September 2</figcaption>
      </figure>

      <p>To ensure accuracy, we validated our satellite-derived flood maps against official government damage assessments and
        ground survey data. The comparison showed remarkable agreement, with our maps achieving over <span class="highlight">90% accuracy</span> in flood boundary delineation. Notably, our satellite analysis identified several flooded areas that weren't immediately apparent in initial ground reports, demonstrating the value of comprehensive space-based monitoring.</p>
      
      <p>The validation process confirmed that combining C-band and L-band SAR data significantly improved detection accuracy compared to using either frequency alone—a finding that has important implications for future flood monitoring systems.</p>
    </section>

    <section>
      <h2>Conclusion: From Satellite Data to Saved Lives</h2>
      <p>The 2018 Kerala floods demonstrated both the devastating power of nature and the life-saving potential of satellite technology. Our analysis proves that space-based flood monitoring isn't just about creating pretty maps—it's about turning data into decisive action when every hour matters.</p>
      
      <p>With 90% accuracy in flood detection and the ability to map over 400 square kilometers of inundation in near real-time, satellite SAR technology could have revolutionized the emergency response. Imagine rescue teams knowing exactly where 40,000 people were stranded across 14 districts, not through desperate phone calls or helicopter surveys, but through precise satellite intelligence delivered within hours of the flooding.</p>
      
      <p>The numbers tell the story: Kerala's 2018 floods claimed over 400 lives and displaced 1.4 million people. While we can't change the past, we can transform the future. Real-time satellite monitoring means faster evacuations from high-risk zones, optimized deployment of rescue boats and helicopters, and strategic positioning of relief supplies before roads become impassable.</p>
      
      <p>In an era where climate change makes extreme weather the new normal, satellite-based flood monitoring isn't a luxury—it's a necessity. The technology exists, the data is available, and the algorithms work. Now it's time to integrate these systems into our disaster preparedness framework, because the next time nature unleashes its fury, we'll be watching from space and ready to respond from the ground.</p>
      
      <p><strong>When satellites save lives, every pixel counts.</strong></p>
    </section>

    <footer>
      <p class="small">&copy; Blog based on published research article co-authored by Dr. Mohamed Musthafa in the journal of Current Science during his tenure @IIT Bombay (2021)</p>
    </footer>
  </article>
</div>
</body>
</html>"""

    # Write the HTML file
    try:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(html_content)
        
        print(f"\n✅ Success! Generated: {output_file}")
        print(f"📂 File size: {os.path.getsize(output_file) / 1024:.1f} KB")
        print(f"🌐 Open {output_file} in your browser to view the blog")
        print("\n📤 Ready to host online:")
        print("   • Drag & drop to netlify.com/drop")
        print("   • Upload to GitHub Pages") 
        print("   • Use with any web hosting service")
        
    except Exception as e:
        print(f"❌ Error writing file: {e}")

if __name__ == "__main__":
    print("🛰️  Kerala Floods Blog Generator")
    print("=" * 40)
    main()