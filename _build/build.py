"""12moon.games static site generator.

Run: python -I build.py <output_dir>
Every page shares one header/footer; content lives in PAGES below.
"""
import sys
from pathlib import Path

OUT = Path(sys.argv[1])
SITE = "https://12moon.games"
EMAIL = "aytugbengu2000@gmail.com"
ADSENSE = "ca-pub-6252919364842437"
UPDATED = "14 November 2026"

CSS = """
:root{--bg:#0b1020;--panel:#121a33;--line:#24305a;--fg:#e9edf7;--muted:#a7b0c8;--accent:#6ea8ff;--accent2:#ffd36e}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--fg);font:17px/1.65 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}
a{color:var(--accent)}
a:hover{color:#9cc3ff}
header.site{border-bottom:1px solid var(--line);background:rgba(11,16,32,.9);position:sticky;top:0;z-index:5;backdrop-filter:blur(6px)}
header.site .wrap{display:flex;align-items:center;gap:20px;flex-wrap:wrap;padding-top:12px;padding-bottom:12px}
.brand{display:flex;align-items:center;gap:10px;color:var(--fg);text-decoration:none;font-weight:700;font-size:1.1rem}
.brand svg{width:30px;height:30px}
nav.main{display:flex;gap:18px;flex-wrap:wrap;margin-left:auto}
nav.main a{color:var(--muted);text-decoration:none;font-size:.95rem}
nav.main a:hover,nav.main a[aria-current]{color:var(--fg)}
.wrap{max-width:900px;margin:0 auto;padding:0 16px}
main{padding:36px 0 64px}
h1{font-size:2rem;line-height:1.25;margin:0 0 12px}
h2{font-size:1.4rem;margin:40px 0 10px}
h3{font-size:1.1rem;margin:26px 0 6px}
p,li{color:var(--fg)}
.lead{font-size:1.15rem;color:var(--muted);margin-bottom:24px}
.muted{color:var(--muted)}
.crumbs{font-size:.9rem;color:var(--muted);margin-bottom:14px}
.crumbs a{color:var(--muted)}
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:16px;margin:20px 0}
.card{background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:18px}
.card h3{margin-top:0}
.card p{margin:0 0 10px;color:var(--muted)}
.tag{display:inline-block;font-size:.8rem;padding:2px 10px;border-radius:999px;background:#1d2a52;color:var(--accent2);margin-bottom:8px}
ol.steps{padding-left:22px}
ol.steps li{margin:0 0 10px}
.note{border-left:3px solid var(--accent2);background:#151d39;padding:12px 16px;border-radius:0 10px 10px 0;margin:18px 0}
code,kbd{background:#1a2445;border:1px solid var(--line);border-radius:6px;padding:1px 6px;font-size:.92em}
table{border-collapse:collapse;width:100%;margin:14px 0}
th,td{border-bottom:1px solid var(--line);padding:8px 6px;text-align:left;vertical-align:top}
th{color:var(--muted);font-weight:600}
.btn{display:inline-block;background:var(--accent);color:#0b1020;text-decoration:none;font-weight:700;padding:10px 18px;border-radius:10px;margin:6px 8px 6px 0}
.btn.ghost{background:transparent;color:var(--fg);border:1px solid var(--line)}
.hero{padding:20px 0 10px}
footer.site{border-top:1px solid var(--line);color:var(--muted);font-size:.9rem;padding:24px 0 40px}
footer.site a{color:var(--muted)}
footer.site .cols{display:flex;gap:24px;flex-wrap:wrap;justify-content:space-between}
@media (max-width:600px){h1{font-size:1.6rem}nav.main{margin-left:0}}
"""

LOGO = """<svg viewBox="0 0 64 64" aria-hidden="true"><defs><linearGradient id="g" x1="0" x2="1" y1="0" y2="1"><stop offset="0" stop-color="#ffd36e"/><stop offset="1" stop-color="#f5a623"/></linearGradient></defs><circle cx="32" cy="32" r="30" fill="#121a33" stroke="#24305a" stroke-width="2"/><path d="M40 14a20 20 0 1 0 10 32 16 16 0 1 1-10-32z" fill="url(#g)"/><text x="22" y="40" font-family="system-ui,sans-serif" font-size="15" font-weight="800" fill="#0b1020">12</text></svg>"""

NAV = [("/", "Home"), ("/tv-mirror/", "TV Mirror"), ("/games/", "Games"), ("/about/", "About"), ("/contact/", "Contact")]


def page(path, title, description, body, lang="en", section=None):
    nav = "".join(
        f'<a href="{href}"{" aria-current=\"page\"" if section == href else ""}>{label}</a>' for href, label in NAV
    )
    html = f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<meta name="google-adsense-account" content="{ADSENSE}">
<link rel="canonical" href="{SITE}{path}">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:type" content="website">
<meta property="og:url" content="{SITE}{path}">
<link rel="stylesheet" href="/style.css">
</head>
<body>
<header class="site"><div class="wrap">
<a class="brand" href="/">{LOGO}<span>12 Moon Games</span></a>
<nav class="main" aria-label="Main">{nav}</nav>
</div></header>
<main><div class="wrap">
{body}
</div></main>
<footer class="site"><div class="wrap cols">
<div>© 2026 12 Moon Games · Independent apps and games from Istanbul, Türkiye</div>
<div><a href="/privacy/">Privacy</a> · <a href="/tv-mirror/privacy/">TV Mirror privacy</a> · <a href="/tv-mirror/terms/">TV Mirror terms</a> · <a href="/contact/">Contact</a></div>
</div></footer>
</body>
</html>
"""
    dest = OUT / path.strip("/") / "index.html" if path != "/" else OUT / "index.html"
    if path.endswith(".html"):
        dest = OUT / path.strip("/")
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(html, encoding="utf-8")
    return path


TVM_CRUMB = '<div class="crumbs"><a href="/">Home</a> › <a href="/tv-mirror/">TV Mirror</a></div>'
GUIDES = """<div class="cards">
<div class="card"><span class="tag">Apple</span><h3><a href="/tv-mirror/iphone-ipad/">iPhone &amp; iPad</a></h3><p>Mirror with Screen Mirroring in Control Center.</p></div>
<div class="card"><span class="tag">Apple</span><h3><a href="/tv-mirror/mac/">Mac</a></h3><p>Use your TV as a mirrored or extended display.</p></div>
<div class="card"><span class="tag">Windows</span><h3><a href="/tv-mirror/windows/">Windows PC</a></h3><p>Share your screen from Chrome or Edge. No install.</p></div>
<div class="card"><span class="tag">Android</span><h3><a href="/tv-mirror/android/">Android phone &amp; tablet</a></h3><p>Use the Cast button that is already on your phone.</p></div>
</div>"""

PAGES = []

# ------------------------------------------------------------------ home
PAGES.append(page("/", "12 Moon Games – apps and games for your TV and phone",
    "12 Moon Games is a small independent studio making TV Mirror, a screen mirroring app for Android TV and Google TV, and casual mobile games.",
f"""<section class="hero">
<h1>Small studio, big screens.</h1>
<p class="lead">12 Moon Games is an independent studio from Istanbul. We make simple, polished apps for your TV and fun games for your phone.</p>
<a class="btn" href="/tv-mirror/">Meet TV Mirror</a><a class="btn ghost" href="/games/">Our games</a>
</section>

<h2>TV Mirror: Screen Mirroring</h2>
<p>TV Mirror turns an Android TV or Google TV into a screen mirroring receiver. Show your iPhone, iPad, Mac, Windows PC or Android phone on the big screen over your home Wi-Fi, without installing anything on the device you are mirroring from. It is built for smooth, stutter-free video and clear stereo sound.</p>
<p><span class="tag">Coming soon to Google Play</span></p>
<p>New to screen mirroring? Our step-by-step guides explain exactly what to tap on each device:</p>
{GUIDES}
<p>Something not working? Start with the <a href="/tv-mirror/troubleshooting/">troubleshooting guide</a> or the <a href="/tv-mirror/faq/">frequently asked questions</a>.</p>

<h2>Games</h2>
<div class="cards">
<div class="card"><span class="tag">In development</span><h3><a href="/games/horror-mall/">Horror Mall</a></h3><p>Trapped in an abandoned shopping mall at night. Find twelve fuel cans and escape before the creatures find you.</p></div>
<div class="card"><span class="tag">In development</span><h3><a href="/games/toilet-survivor/">Toilet Survivor</a></h3><p>A chaotic two-player action shooter. Hold your ground against wave after wave in very tight spaces.</p></div>
</div>

<h2>How we work</h2>
<p>We are a tiny team, so every app gets the same treatment: do one thing well, keep it fast, and respect your privacy. Our apps collect as little as possible; you can read exactly what each one does in its privacy policy. If you have an idea, a bug report or just want to say hi, <a href="/contact/">get in touch</a>. We read everything.</p>
""", section="/"))

# ------------------------------------------------------------------ tv mirror overview
PAGES.append(page("/tv-mirror/", "TV Mirror – screen mirroring for Android TV and Google TV",
    "TV Mirror lets you mirror iPhone, iPad, Mac, Windows PC and Android screens to an Android TV or Google TV over Wi-Fi, with nothing to install on the sending device.",
f"""<div class="crumbs"><a href="/">Home</a> › TV Mirror</div>
<h1>TV Mirror: Screen Mirroring</h1>
<p class="lead">Mirror your phone, tablet or computer to your TV. Smoothly, over your home Wi-Fi, with nothing to install on the device you mirror from.</p>
<p><span class="tag">Coming soon to Google Play · Android TV &amp; Google TV</span></p>

<h2>What it does</h2>
<p>TV Mirror is an app you install on your TV, not on your phone. Once it is open, your TV shows up in the screen mirroring menus that are already built into your devices:</p>
<ul>
<li><strong>iPhone, iPad and Mac:</strong> the TV appears in <em>Screen Mirroring</em>, the same menu you would use for an Apple TV.</li>
<li><strong>Windows PC:</strong> open the address shown on the TV in Chrome or Edge and press <em>Share screen</em>. There is no program to download.</li>
<li><strong>Android phones and tablets:</strong> use the <em>Cast</em> or <em>Screen Cast</em> button in Quick Settings. This uses the Google Cast receiver built into Android TV and Google TV, and TV Mirror shows you how to find it.</li>
</ul>

<h2>Step-by-step guides</h2>
{GUIDES}
<p>Türkçe kurulum rehberi için: <a href="/tv-mirror/tr/">TV Mirror Türkçe kullanım rehberi</a>.</p>

<h2>Built for smooth playback</h2>
<p>Screen mirroring over Wi-Fi has to deal with a network that is never perfectly steady. Many mirroring apps try to show every frame the instant it arrives, which looks fine for a second and then stutters whenever Wi-Fi hiccups. TV Mirror deliberately keeps a small, steady buffer, usually well under a second, and plays frames at an even pace. The result is a picture that stays smooth during videos, presentations and games, with sound kept in sync with the image.</p>
<table>
<tr><th>From</th><th>How it connects</th><th>Picture</th><th>Sound</th></tr>
<tr><td>iPhone, iPad</td><td>Screen Mirroring (Control Center)</td><td>Up to the device's mirroring resolution</td><td>Yes</td></tr>
<tr><td>Mac</td><td>Screen Mirroring (Control Center / menu bar)</td><td>Up to 1080p</td><td>Yes</td></tr>
<tr><td>Windows PC</td><td>Chrome or Edge, address shown on the TV</td><td>Up to 1080p, up to 60 fps</td><td>Yes, lossless stereo when you share system audio</td></tr>
<tr><td>Android</td><td>Cast / Screen Cast (Google Cast built into the TV)</td><td>Handled by Google Cast</td><td>Handled by Google Cast</td></tr>
</table>

<h2>Requirements</h2>
<ul>
<li>An Android TV or Google TV running Android 8.0 or newer.</li>
<li>The TV and the device you mirror from on the <strong>same Wi-Fi network</strong>.</li>
<li>TV Mirror <strong>open on the TV</strong> while you mirror. It does not run in the background, so when you close it your TV disappears from the lists.</li>
<li>For Windows: an up-to-date Google Chrome or Microsoft Edge.</li>
</ul>

<h2>Privacy by design</h2>
<p>Your screen and sound travel directly from your device to your TV inside your home network. They are never sent to us or to any server, recorded or stored. TV Mirror has no accounts and no cloud service. Details are in the <a href="/tv-mirror/privacy/">TV Mirror privacy policy</a> and the <a href="/tv-mirror/terms/">terms of service</a>.</p>

<h2>Need help?</h2>
<p>See <a href="/tv-mirror/troubleshooting/">troubleshooting</a> and the <a href="/tv-mirror/faq/">FAQ</a>, or <a href="/contact/">contact us</a>.</p>
""", section="/tv-mirror/"))

# ------------------------------------------------------------------ iphone
PAGES.append(page("/tv-mirror/iphone-ipad/", "How to mirror an iPhone or iPad to Android TV – TV Mirror guide",
    "Step-by-step: mirror your iPhone or iPad screen to an Android TV or Google TV with TV Mirror and Screen Mirroring in Control Center.",
f"""{TVM_CRUMB}
<h1>Mirror an iPhone or iPad to your TV</h1>
<p class="lead">You don't need an Apple TV or any extra app on your iPhone. TV Mirror makes your Android TV or Google TV appear in the iPhone's own Screen Mirroring menu.</p>

<h2>Before you start</h2>
<ul>
<li>Connect the iPhone or iPad and the TV to the <strong>same Wi-Fi network</strong>. A guest network usually will not work, because guest networks keep devices from seeing each other.</li>
<li>Open <strong>TV Mirror</strong> on the TV and leave it on its home screen. The top of the screen shows <em>Ready to mirror</em> and the name your TV uses.</li>
</ul>

<h2>Steps</h2>
<ol class="steps">
<li>Open <strong>Control Center</strong>. On iPhones without a Home button, swipe down from the top-right corner. On models with a Home button, swipe up from the bottom edge.</li>
<li>Tap <strong>Screen Mirroring</strong>, the icon with two overlapping rectangles.</li>
<li>Choose your TV from the list. It appears with the name shown on the TV, followed by <em>(TV Mirror)</em>, for example <code>Living Room (TV Mirror)</code>.</li>
<li>Your screen appears on the TV within a few seconds. Turn the phone sideways to fill the screen when watching videos or photos.</li>
</ol>

<h2>Stop mirroring</h2>
<p>Open Control Center again, tap <strong>Screen Mirroring</strong> and then <strong>Stop Mirroring</strong>. Closing TV Mirror on the TV also ends the session.</p>

<h2>Tips</h2>
<ul>
<li><strong>Sound:</strong> audio plays through the TV while mirroring. Use the TV remote for volume.</li>
<li><strong>Portrait vs. landscape:</strong> in portrait, the TV shows your screen in the middle with bars on the sides. This is normal, because the image keeps its shape and is never stretched.</li>
<li><strong>Protected video:</strong> some streaming apps block screen mirroring for copyright reasons. Their video may stay black or the app may refuse to play while mirroring. This is decided by the app, not by TV Mirror.</li>
<li><strong>Do Not Disturb:</strong> notifications are mirrored too. Turn on a Focus mode if you are presenting.</li>
</ul>

<div class="note">TV not in the list? Check that TV Mirror is open on the TV, that both devices are on the same Wi-Fi, and see <a href="/tv-mirror/troubleshooting/">troubleshooting</a>.</div>
""", section="/tv-mirror/"))

# ------------------------------------------------------------------ mac
PAGES.append(page("/tv-mirror/mac/", "How to mirror a Mac to Android TV – TV Mirror guide",
    "Mirror a MacBook or iMac screen to an Android TV or Google TV with TV Mirror and macOS Screen Mirroring, or use the TV as a second display.",
f"""{TVM_CRUMB}
<h1>Mirror a Mac to your TV</h1>
<p class="lead">MacBook, iMac or Mac mini: your Mac can send its screen to the TV with the Screen Mirroring feature that is already part of macOS.</p>

<h2>Before you start</h2>
<ul>
<li>The Mac and the TV must be on the same Wi-Fi network.</li>
<li>Open <strong>TV Mirror</strong> on the TV and keep it open.</li>
</ul>

<h2>Steps</h2>
<ol class="steps">
<li>Click <strong>Control Center</strong> in the menu bar at the top right of the screen (the icon with two toggles).</li>
<li>Click <strong>Screen Mirroring</strong>.</li>
<li>Select your TV, shown as <em>TV name (TV Mirror)</em>.</li>
<li>Choose <strong>Mirror Built-in Display</strong> to show the same picture on both screens, or <strong>Use As Separate Display</strong> to extend your desktop onto the TV, which is great for presentations or keeping a video on the TV while you work.</li>
</ol>

<h2>Picture and sound</h2>
<p>The TV shows your Mac at up to 1080p. Sound switches to the TV automatically while mirroring. If it doesn't, open <strong>System Settings › Sound › Output</strong> and pick the TV.</p>
<p>For the sharpest text, open <strong>System Settings › Displays</strong>, select the TV and choose a resolution that matches it, for example 1920 × 1080.</p>

<h2>Stop mirroring</h2>
<p>Open Control Center › Screen Mirroring and click your TV again to disconnect, or simply close TV Mirror on the TV.</p>

<div class="note">Using a work Mac? Some company-managed Macs turn off Screen Mirroring. In that case the option is greyed out and only your IT department can enable it.</div>
""", section="/tv-mirror/"))

# ------------------------------------------------------------------ windows
PAGES.append(page("/tv-mirror/windows/", "How to mirror a Windows PC to Android TV from Chrome or Edge – TV Mirror guide",
    "Mirror a Windows laptop or PC to an Android TV or Google TV from Chrome or Edge with TV Mirror. No software to install; includes system audio.",
f"""{TVM_CRUMB}
<h1>Mirror a Windows PC to your TV</h1>
<p class="lead">No download, no driver, no account. Your browser does the work: TV Mirror runs a small web page on your TV that your PC opens over Wi-Fi.</p>

<h2>Before you start</h2>
<ul>
<li>Use <strong>Google Chrome</strong> or <strong>Microsoft Edge</strong> on Windows 10 or 11, updated to the latest version.</li>
<li>Connect the PC and the TV to the same Wi-Fi network, or plug the PC into the same router with a cable.</li>
<li>Open <strong>TV Mirror</strong> on the TV. In the Windows card it shows an address such as <code>192.168.1.20:9443</code>. Yours will be different.</li>
</ul>

<h2>Steps</h2>
<ol class="steps">
<li>In Chrome or Edge, type the address shown on the TV into the address bar exactly as shown, including <code>:9443</code>, and press Enter. You do not need to type <code>https://</code>.</li>
<li>The first time, the browser shows a privacy or certificate warning. Click <strong>Advanced</strong> and then <strong>Proceed</strong> (Chrome) or <strong>Continue</strong> (Edge). <a href="#certificate">Why does this appear?</a></li>
<li>The TV Mirror page opens. Click <strong>Share screen</strong>.</li>
<li>In the window that opens, choose <strong>Entire screen</strong>, tick <strong>Also share system audio</strong> if you want sound, and click <strong>Share</strong>.</li>
<li>Your screen appears on the TV. To stop, click <strong>Stop sharing</strong> in the bar at the bottom of the screen or close the tab.</li>
</ol>

<h2 id="certificate">About the certificate warning</h2>
<p>Browsers only allow screen sharing on secure (HTTPS) pages. A website on the internet gets its security certificate from a public authority, but your TV is a device in your own home with a private address like 192.168.x.x, which no public authority can certify. TV Mirror therefore creates its own certificate on the TV, and the browser warns you because it doesn't recognise who issued it.</p>
<p>The connection is still encrypted and stays inside your home network. You only need to accept the warning once per browser. If you ever see this warning for an address that is <em>not</em> the one shown on your TV, don't continue.</p>

<h2>Getting the best result</h2>
<ul>
<li><strong>Sound:</strong> audio is sent only if you tick <em>Also share system audio</em> when sharing the <em>entire screen</em>. Sharing a single window cannot include system sound; this is a browser limit.</li>
<li><strong>Smoothness:</strong> TV Mirror uses your PC's hardware video encoder and sends up to 60 frames per second. If the picture stutters, move closer to the router, use 5 GHz Wi-Fi, or connect the PC with a cable.</li>
<li><strong>Presentations:</strong> share a single browser tab or window if you only want to show one thing and keep the rest of your screen private.</li>
<li><strong>Protected video:</strong> streaming services that use copy protection may show a black area when shared. That is the service's choice, not a TV Mirror problem.</li>
</ul>

<div class="note">Page doesn't open? Check the address and the <code>:9443</code> part, make sure both devices are on the same network, and see <a href="/tv-mirror/troubleshooting/">troubleshooting</a>.</div>
""", section="/tv-mirror/"))

# ------------------------------------------------------------------ android
PAGES.append(page("/tv-mirror/android/", "How to mirror an Android phone to Android TV or Google TV – TV Mirror guide",
    "Mirror an Android phone or tablet to an Android TV or Google TV using the built-in Cast / Screen Cast button and Google Cast.",
f"""{TVM_CRUMB}
<h1>Mirror an Android phone or tablet to your TV</h1>
<p class="lead">Good news: Android TV and Google TV already have a Google Cast receiver built in. Your phone can cast its screen to it directly, and TV Mirror's home screen shows you how.</p>

<h2>Steps</h2>
<ol class="steps">
<li>Make sure the phone and the TV are on the same Wi-Fi network.</li>
<li>Swipe down from the top of the screen twice to open <strong>Quick Settings</strong>.</li>
<li>Tap <strong>Screen Cast</strong>, <strong>Cast</strong> or, on Samsung phones, <strong>Smart View</strong>. If you don't see it, tap the pencil (edit) icon and drag the tile into Quick Settings.</li>
<li>Choose your TV from the list and confirm with <strong>Start now</strong>.</li>
</ol>

<h2>If the Cast button is missing</h2>
<ol class="steps">
<li>Install or open the <strong>Google Home</strong> app on your phone.</li>
<li>Select your TV, or add it if it isn't listed yet.</li>
<li>Tap <strong>Cast my screen</strong>.</li>
</ol>

<h2>Good to know</h2>
<ul>
<li>Android mirroring is handled by Google Cast on your TV, not by TV Mirror itself. Picture quality and delay therefore depend on Google Cast.</li>
<li>Many video apps such as YouTube have their own Cast button. Using it sends just the video to the TV in full quality, and you can keep using your phone for other things.</li>
<li>Some phone makers rename the feature, for example <em>Smart View</em>, <em>Screen Mirroring</em> or <em>Wireless Projection</em>, but it does the same job.</li>
</ul>
""", section="/tv-mirror/"))

# ------------------------------------------------------------------ troubleshooting
PAGES.append(page("/tv-mirror/troubleshooting/", "TV Mirror troubleshooting – TV not showing, no sound, stutter",
    "Fix common screen mirroring problems with TV Mirror: TV not in the list, Windows page not opening, no sound, black screen, stuttering or delay.",
f"""{TVM_CRUMB}
<h1>Troubleshooting</h1>
<p class="lead">Most mirroring problems come down to three things: the app isn't open on the TV, the devices aren't on the same network, or the network blocks devices from finding each other. Start at the top.</p>

<h2>My TV doesn't appear in the list</h2>
<ol class="steps">
<li><strong>Is TV Mirror open on the TV?</strong> TV Mirror only receives while it is open and on screen. If you pressed Home or opened another app, open it again.</li>
<li><strong>Same network?</strong> Check the Wi-Fi name on both devices. Phones sometimes jump to mobile data or to a neighbouring network. Dual-band routers are fine: a phone on 5 GHz and a TV on 2.4 GHz from the same router can see each other.</li>
<li><strong>Guest network or "client isolation"?</strong> Guest Wi-Fi and some office or hotel networks stop devices from talking to each other. Use your main home network, or turn off <em>AP isolation</em> / <em>client isolation</em> in the router settings.</li>
<li><strong>VPN on the phone or computer?</strong> Some VPN apps block local network traffic. Pause the VPN and try again.</li>
<li><strong>Restart the basics.</strong> Turn Wi-Fi off and on again on the phone, close and reopen TV Mirror, and if needed restart the router.</li>
</ol>
<p>Mesh Wi-Fi systems and some routers filter the "announcement" messages that iPhones and Macs use to find nearby screens. If your TV still doesn't appear, check the router for settings called <em>multicast</em>, <em>mDNS</em> or <em>IGMP snooping</em>.</p>

<h2>The Windows page doesn't open</h2>
<ul>
<li>Type the address exactly as shown on the TV, including the number after the colon (<code>:9443</code>).</li>
<li>Use Chrome or Edge. Other browsers may not support the screen-sharing features TV Mirror needs.</li>
<li>If Windows asks whether to allow the network to be found, choose <em>Private network</em>. Some security programs block local connections, so try pausing them briefly.</li>
<li>The TV's address can change after a router restart. Always use the one currently shown on the TV.</li>
</ul>

<h2>There is no sound</h2>
<ul>
<li><strong>Windows:</strong> share the <em>Entire screen</em> and tick <em>Also share system audio</em>. Without that tick the browser sends no sound.</li>
<li><strong>iPhone/iPad:</strong> check the ring/silent switch and volume, and that the app you're using actually plays sound.</li>
<li><strong>TV:</strong> check the TV volume and that it isn't muted or set to an external speaker that is switched off.</li>
</ul>

<h2>The picture is black</h2>
<p>Apps and websites that play copy-protected video (many movie and TV services) block screen capture. You will see a black area or an error, while everything else mirrors normally. This protection is enforced by the app or website, so no mirroring app can show that content. Use the app's own Cast button or the app on your TV instead.</p>

<h2>The picture stutters or freezes</h2>
<ul>
<li>Move the router, the TV or the phone closer, or remove obstacles between them.</li>
<li>Prefer 5 GHz Wi-Fi, and connect the TV with an Ethernet cable if it has a port.</li>
<li>Large downloads or other streams on the same network compete for bandwidth.</li>
</ul>

<h2>There is a short delay</h2>
<p>That is intentional. TV Mirror keeps a small buffer, usually well under a second, so that short Wi-Fi hiccups don't turn into stutters. For video, photos and presentations this gives a much smoother result. Fast action games are better played on a wired connection or directly on the TV.</p>

<h2>Still stuck?</h2>
<p>Write to us at <a href="mailto:{EMAIL}">{EMAIL}</a>. Tell us your TV model, what you're mirroring from and what you see, and we'll help.</p>
""", section="/tv-mirror/"))

# ------------------------------------------------------------------ faq
PAGES.append(page("/tv-mirror/faq/", "TV Mirror FAQ – screen mirroring questions answered",
    "Answers to common questions about TV Mirror: price, supported devices, internet use, privacy, picture quality, delay and more.",
f"""{TVM_CRUMB}
<h1>Frequently asked questions</h1>

<h3>Is TV Mirror free?</h3>
<p>Yes, TV Mirror is free to download and use. Some versions may show a short video ad when the app opens. Ads never appear while you are mirroring, and an optional one-time purchase removes them.</p>

<h3>Do I need to install anything on my phone or computer?</h3>
<p>No. iPhone, iPad and Mac use their built-in Screen Mirroring, Windows uses Chrome or Edge, and Android uses its built-in Cast feature. TV Mirror is installed only on the TV.</p>

<h3>Which TVs are supported?</h3>
<p>TVs and streaming boxes running Android TV or Google TV, version 8.0 or newer. That includes most Sony, TCL, Philips, Hisense, Grundig and Xiaomi Android TVs, Chromecast with Google TV and many other Google TV devices.</p>

<h3>Does it need the internet?</h3>
<p>Mirroring works inside your home network. Your screen is not sent over the internet. An internet connection is only needed to download the app and, in versions that show ads, to load the ad.</p>

<h3>Is my screen recorded or uploaded?</h3>
<p>No. The picture and sound go straight from your device to your TV and are never stored or sent to us. See the <a href="/tv-mirror/privacy/">privacy policy</a>.</p>

<h3>Why is there a small delay?</h3>
<p>TV Mirror buffers a fraction of a second on purpose to keep playback smooth on everyday Wi-Fi. See <a href="/tv-mirror/troubleshooting/">troubleshooting</a> for details.</p>

<h3>What picture quality can I expect?</h3>
<p>Up to 1080p. From Windows up to 60 frames per second with lossless stereo sound; from Apple devices at the quality they send for Screen Mirroring.</p>

<h3>Can two people mirror at the same time?</h3>
<p>TV Mirror shows one device at a time. When a new device starts mirroring, it takes over from the previous one.</p>

<h3>Does it work when the app is closed?</h3>
<p>No. For privacy, TV Mirror only receives while it is open on the screen. When you close it, the TV disappears from the mirroring lists.</p>

<h3>Is TV Mirror made by Apple, Google or Microsoft?</h3>
<p>No. TV Mirror is an independent app by 12 Moon Games and is not affiliated with or endorsed by Apple, Google or Microsoft. Product names belong to their owners.</p>
""", section="/tv-mirror/"))

# ------------------------------------------------------------------ turkish guide
PAGES.append(page("/tv-mirror/tr/", "TV Mirror Türkçe rehber – Android TV'ye ekran yansıtma",
    "TV Mirror ile iPhone, iPad, Mac, Windows bilgisayar ve Android telefon ekranını Android TV veya Google TV'ye yansıtma rehberi.",
"""<div class="crumbs"><a href="/">Ana sayfa</a> › <a href="/tv-mirror/">TV Mirror</a> › Türkçe</div>
<h1>TV Mirror: Ekran Yansıtma rehberi</h1>
<p class="lead">TV Mirror'ı yalnızca TV'nize kurarsınız. Telefonunuza veya bilgisayarınıza hiçbir şey kurmadan, ev Wi-Fi'nizden ekranınızı TV'ye yansıtırsınız.</p>

<h2>Başlamadan önce</h2>
<ul>
<li>TV ile yansıtacağınız cihaz <strong>aynı Wi-Fi ağında</strong> olmalı. Misafir ağlarında çalışmayabilir.</li>
<li>TV'de <strong>TV Mirror açık</strong> olmalı. Uygulama kapalıyken TV listelerde görünmez.</li>
</ul>

<h2>iPhone ve iPad</h2>
<ol class="steps">
<li><strong>Denetim Merkezi</strong>'ni açın (sağ üst köşeden aşağı kaydırın).</li>
<li><strong>Ekran Yansıtma</strong>'ya dokunun.</li>
<li>Listeden <em>TV adı (TV Mirror)</em> şeklinde görünen TV'nizi seçin.</li>
</ol>

<h2>Mac</h2>
<ol class="steps">
<li>Menü çubuğunda <strong>Denetim Merkezi › Ekran Yansıtma</strong>'yı açın.</li>
<li>TV'nizi seçin; aynı görüntü için <em>Yerleşik Ekranı Yansıt</em>, masaüstünü genişletmek için <em>Ayrı Ekran Olarak Kullan</em>'ı seçin.</li>
</ol>

<h2>Windows bilgisayar</h2>
<ol class="steps">
<li>Chrome veya Edge'de, TV'de yazan adresi (ör. <code>192.168.1.20:9443</code>) adres çubuğuna yazın.</li>
<li>İlk seferde çıkan güvenlik uyarısında <strong>Gelişmiş › Devam et</strong>'e tıklayın. TV'niz evinizdeki özel bir cihaz olduğu için tarayıcı sertifikayı tanımaz; bağlantı yine şifrelidir ve evinizin içinde kalır.</li>
<li><strong>Ekranı paylaş</strong>'a basın, <em>Tüm ekran</em>'ı seçin; ses için <em>Sistem sesini de paylaş</em>'ı işaretleyin.</li>
</ol>

<h2>Android telefon ve tablet</h2>
<ol class="steps">
<li>Hızlı Ayarlar'ı açın (üstten iki kez aşağı kaydırın).</li>
<li><strong>Ekran Yayınla</strong>, <strong>Yayınla</strong> veya Samsung'da <strong>Smart View</strong>'a dokunun ve TV'nizi seçin.</li>
<li>Düğme yoksa <strong>Google Home</strong> uygulamasında TV'nizi seçip <strong>Ekranımı yayınla</strong>'ya dokunun.</li>
</ol>

<h2>Sorun mu var?</h2>
<ul>
<li><strong>TV listede yok:</strong> TV Mirror'ın açık olduğundan, iki cihazın aynı ağda olduğundan emin olun; telefondaki VPN'i kapatın, Wi-Fi'yi kapatıp açın.</li>
<li><strong>Windows'ta ses yok:</strong> <em>Tüm ekran</em>'ı seçip <em>Sistem sesini de paylaş</em>'ı işaretleyin.</li>
<li><strong>Siyah görüntü:</strong> Telif korumalı video uygulamaları ekran yansıtmayı engeller; bu uygulamanın kendi tercihidir.</li>
<li><strong>Kısa gecikme:</strong> Görüntünün takılmaması için bilerek saniyenin altında küçük bir tampon kullanılır.</li>
</ul>
<p>Yardım için: <a href="mailto:aytugbengu2000@gmail.com">aytugbengu2000@gmail.com</a> · <a href="/tv-mirror/privacy/">Gizlilik politikası</a> · <a href="/tv-mirror/terms/">Kullanım koşulları</a></p>
""", lang="tr", section="/tv-mirror/"))

# ------------------------------------------------------------------ games
PAGES.append(page("/games/", "Games by 12 Moon Games",
    "Mobile games in development at 12 Moon Games: Horror Mall, a co-op horror escape, and Toilet Survivor, a two-player action shooter.",
"""<div class="crumbs"><a href="/">Home</a> › Games</div>
<h1>Games</h1>
<p class="lead">Short sessions, simple controls and plenty of personality. Here is what we are working on.</p>
<div class="cards">
<div class="card"><span class="tag">In development · Horror</span><h3><a href="/games/horror-mall/">Horror Mall</a></h3><p>Escape an abandoned mall at night by finding twelve fuel cans, alone or with a friend.</p></div>
<div class="card"><span class="tag">In development · Action</span><h3><a href="/games/toilet-survivor/">Toilet Survivor</a></h3><p>A two-player action shooter where every square metre counts.</p></div>
</div>
<p>Want to try our games before release? <a href="/contact/">Write to us</a> and we'll add you to the test group on Google Play.</p>
""", section="/games/"))

PAGES.append(page("/games/horror-mall/", "Horror Mall – co-op horror escape game",
    "Horror Mall is a mobile horror escape game: trapped in an abandoned shopping mall, find twelve fuel cans to start the car and escape the creatures.",
"""<div class="crumbs"><a href="/">Home</a> › <a href="/games/">Games</a></div>
<h1>Horror Mall</h1>
<p class="lead">You are trapped inside an abandoned shopping mall. The only way out is a car in the parking lot, but its tank is empty.</p>
<p><span class="tag">In development for Android</span></p>
<h2>The goal</h2>
<p>Search the dark shops, corridors and service rooms for <strong>twelve fuel cans</strong>. Carry each one back, fill the car and get out before the night is over. Sounds simple, until you hear something moving in the next aisle.</p>
<h2>Survive the creatures</h2>
<p>Mysterious creatures roam the halls and they will do anything to stop you. Stay out of sight, listen carefully and pick your route. Running makes noise; hiding takes time. Every can you find makes the mall a little more dangerous.</p>
<h2>Better together</h2>
<p>Play alone or team up with a friend in co-op. Split up to search faster, or stick together and watch each other's backs.</p>
<h2>Features</h2>
<ul>
<li>Dark, tense atmosphere built for headphones</li>
<li>Twelve fuel cans hidden across the mall: find them all to escape</li>
<li>Simple, intuitive touch controls</li>
<li>Smooth performance tuned for phones</li>
</ul>
""", section="/games/"))

PAGES.append(page("/games/toilet-survivor/", "Toilet Survivor – two-player action shooter",
    "Toilet Survivor is a chaotic two-player action shooter: defend yourself against waves of enemies in tight spaces and become the ultimate survivor.",
"""<div class="crumbs"><a href="/">Home</a> › <a href="/games/">Games</a></div>
<h1>Toilet Survivor</h1>
<p class="lead">An action shooter set somewhere no hero ever wanted to be. Hold the line, wave after wave.</p>
<p><span class="tag">In development for Android</span></p>
<h2>How it plays</h2>
<p>Enemies keep coming and there is very little room to move. Toilet Survivor is about positioning: find the best corner, watch your angles and make every shot count. Each wave is a little faster and a little meaner than the last.</p>
<h2>Two players</h2>
<p>Team up with a friend and split the work: one holds the door while the other covers the flank. Coordination beats firepower.</p>
<h2>Features</h2>
<ul>
<li>Fast, wave-based action in tight spaces</li>
<li>Two-player mode</li>
<li>Strategy and reflexes in equal measure</li>
<li>Short rounds that are perfect for a quick break</li>
</ul>
""", section="/games/"))

# ------------------------------------------------------------------ about / contact / privacy
PAGES.append(page("/about/", "About 12 Moon Games",
    "12 Moon Games is a small independent studio from Istanbul, Türkiye, making TV Mirror and casual mobile games.",
"""<div class="crumbs"><a href="/">Home</a> › About</div>
<h1>About 12 Moon Games</h1>
<p class="lead">We are a small independent studio from Istanbul, Türkiye, founded by developer Aytuğ Bengü.</p>
<p>12 Moon Games started with small mobile games: quick to learn, fun to share and built by a tiny team that cares about the details. Over time we became just as interested in the screens around the house, which led to <a href="/tv-mirror/">TV Mirror</a>, our app that turns an Android TV or Google TV into a screen mirroring receiver for iPhone, iPad, Mac, Windows and Android.</p>
<h2>What we believe in</h2>
<ul>
<li><strong>Do one thing well.</strong> Each app has a clear purpose and no clutter.</li>
<li><strong>Smooth beats flashy.</strong> We tune for steady performance on everyday hardware and Wi-Fi.</li>
<li><strong>Respect for your privacy.</strong> We collect as little as possible and say exactly what we do.</li>
<li><strong>Listen to players.</strong> Feedback from our users shapes every update.</li>
</ul>
<h2>Where to find us</h2>
<p>Our apps are published on Google Play under the developer name <em>12 Moon Games</em>. For anything else, see the <a href="/contact/">contact page</a>.</p>
""", section="/about/"))

PAGES.append(page("/contact/", "Contact 12 Moon Games",
    "Contact 12 Moon Games for TV Mirror support, game feedback, testing or business enquiries.",
f"""<div class="crumbs"><a href="/">Home</a> › Contact</div>
<h1>Contact</h1>
<p class="lead">We are a small team and we read every message.</p>
<p>Email: <a href="mailto:{EMAIL}">{EMAIL}</a></p>
<h2>TV Mirror support</h2>
<p>To help us help you quickly, please include:</p>
<ul>
<li>Your TV or streaming device model</li>
<li>What you are mirroring from (for example iPhone 15, MacBook, Windows 11 with Chrome)</li>
<li>What you expected and what happened instead</li>
</ul>
<p>Many common issues are already answered in <a href="/tv-mirror/troubleshooting/">troubleshooting</a> and the <a href="/tv-mirror/faq/">FAQ</a>.</p>
<h2>Testers and feedback</h2>
<p>Want to try our games or apps before release? Send us the Google account email you use on Google Play and we'll invite you to the test group.</p>
<h2>Business</h2>
<p>For partnerships, press and other enquiries, use the same address with a short subject line.</p>
""", section="/contact/"))

PAGES.append(page("/privacy/", "Privacy policy – 12moon.games website",
    "Privacy policy for the 12moon.games website: what data is processed when you visit, cookies and Google advertising.",
f"""<div class="crumbs"><a href="/">Home</a> › Privacy</div>
<h1>Website privacy policy</h1>
<p class="muted">Last updated: {UPDATED}. This policy covers the website 12moon.games. Each app has its own policy, for example the <a href="/tv-mirror/privacy/">TV Mirror privacy policy</a>.</p>
<h2>Who we are</h2>
<p>12moon.games is run by 12 Moon Games (Aytuğ Bengü), Istanbul, Türkiye. Contact: <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
<h2>What we collect</h2>
<p>This website has no user accounts, contact forms or analytics of our own. We do not ask for or store personal information. If you email us, we use your message and address only to reply.</p>
<h2>Hosting</h2>
<p>The site is hosted on GitHub Pages. Like any web server, GitHub may process technical data such as your IP address and browser type to deliver the pages and keep the service secure. See <a href="https://docs.github.com/site-policy/privacy-policies/github-general-privacy-statement">GitHub's privacy statement</a>.</p>
<h2>Advertising and cookies</h2>
<p>We use Google AdSense to manage advertising for our apps and may show ads on this website in the future. If ads are shown:</p>
<ul>
<li>Third-party vendors, including Google, use cookies to serve ads based on your prior visits to this website or other websites.</li>
<li>Google's use of advertising cookies enables it and its partners to serve ads to you based on your visits to this and other sites on the internet.</li>
<li>You can opt out of personalised advertising in Google's <a href="https://adssettings.google.com">Ads Settings</a>, or opt out of some third-party vendors' use of cookies at <a href="https://www.aboutads.info/choices/">aboutads.info</a>.</li>
<li>In the EEA, the UK and Switzerland, personalised ads are only shown with your consent.</li>
</ul>
<p>Learn more in <a href="https://policies.google.com/technologies/partner-sites">how Google uses information from sites or apps that use its services</a>.</p>
<h2>Children</h2>
<p>This website is not directed at children under 13.</p>
<h2>Changes</h2>
<p>We will update this page and the date above if this policy changes.</p>
""", section=None))

# ------------------------------------------------------------------ 404
PAGES.append(page("/404.html", "Page not found – 12 Moon Games", "This page does not exist.",
"""<h1>Page not found</h1><p class="lead">The page you are looking for doesn't exist or has moved.</p><p><a class="btn" href="/">Go to the home page</a> <a class="btn ghost" href="/tv-mirror/">TV Mirror</a></p>"""))

# ------------------------------------------------------------------ static files
(OUT / "style.css").write_text(CSS.strip() + "\n", encoding="utf-8")
(OUT / "favicon.svg").write_text(LOGO.replace('aria-hidden="true"', 'xmlns="http://www.w3.org/2000/svg"'), encoding="utf-8")
(OUT / "ads.txt").write_text("google.com, pub-6252919364842437, DIRECT, f08c47fec0942fa0\n", encoding="utf-8")
(OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n", encoding="utf-8")
(OUT / ".nojekyll").write_text("", encoding="utf-8")
urls = [p for p in PAGES if not p.endswith(".html")] + ["/tv-mirror/privacy/", "/tv-mirror/terms/"]
(OUT / "sitemap.xml").write_text(
    '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    + "".join(f"  <url><loc>{SITE}{u}</loc></url>\n" for u in urls)
    + "</urlset>\n",
    encoding="utf-8",
)
print(f"{len(PAGES)} pages ->", OUT)
