"""Generate SVG cover art for 12moon.games (rendered to JPG with headless Chrome)."""
import sys
from pathlib import Path

OUT = Path(sys.argv[1])
OUT.mkdir(parents=True, exist_ok=True)
W, H = 1024, 500


def horror_mall():
    vx, vy0, vy1 = 512, 196, 268  # back wall top/bottom at vanishing area
    bx0, bx1 = 452, 572
    s = []
    s.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">')
    s.append("""<defs>
<radialGradient id="air" cx="50%" cy="46%" r="55%"><stop offset="0" stop-color="#3b3226"/><stop offset=".5" stop-color="#16120e"/><stop offset="1" stop-color="#070605"/></radialGradient>
<linearGradient id="floor" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2a231b"/><stop offset="1" stop-color="#060504"/></linearGradient>
<linearGradient id="wallL" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#050505"/><stop offset="1" stop-color="#1d1915"/></linearGradient>
<linearGradient id="wallR" x1="1" y1="0" x2="0" y2="0"><stop offset="0" stop-color="#050505"/><stop offset="1" stop-color="#1d1915"/></linearGradient>
<radialGradient id="vig" cx="50%" cy="50%" r="72%"><stop offset=".5" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".9"/></radialGradient>
<radialGradient id="eye" r="50%"><stop offset="0" stop-color="#ff5a3c"/><stop offset=".35" stop-color="#d0201a" stop-opacity=".9"/><stop offset="1" stop-color="#d0201a" stop-opacity="0"/></radialGradient>
<radialGradient id="canlight" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#ffb347" stop-opacity=".35"/><stop offset="1" stop-color="#ffb347" stop-opacity="0"/></radialGradient>
<linearGradient id="can" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#5e0f0c"/><stop offset=".35" stop-color="#c4261d"/><stop offset=".55" stop-color="#e2493a"/><stop offset="1" stop-color="#4a0b09"/></linearGradient>
<filter id="blur8"><feGaussianBlur stdDeviation="8"/></filter>
<filter id="blur3"><feGaussianBlur stdDeviation="3"/></filter>
<filter id="grain"><feTurbulence type="fractalNoise" baseFrequency=".9" numOctaves="2" seed="4"/><feColorMatrix values="0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  0 0 0 .07 0"/></filter>
</defs>""")
    s.append(f'<rect width="{W}" height="{H}" fill="url(#air)"/>')
    # ceiling, floor, walls
    s.append(f'<polygon points="0,0 {W},0 {bx1},{vy0} {bx0},{vy0}" fill="#0c0b0a"/>')
    s.append(f'<polygon points="0,{H} {W},{H} {bx1},{vy1} {bx0},{vy1}" fill="url(#floor)"/>')
    s.append(f'<polygon points="0,0 {bx0},{vy0} {bx0},{vy1} 0,{H}" fill="url(#wallL)"/>')
    s.append(f'<polygon points="{W},0 {bx1},{vy0} {bx1},{vy1} {W},{H}" fill="url(#wallR)"/>')
    s.append(f'<rect x="{bx0}" y="{vy0}" width="{bx1-bx0}" height="{vy1-vy0}" fill="#120f0c"/>')
    # floor tile lines converging
    for i in range(-8, 9):
        x = 512 + i * 150
        s.append(f'<line x1="{x}" y1="{H}" x2="{512 + i*7.5:.1f}" y2="{vy1}" stroke="#3a3128" stroke-opacity=".35" stroke-width="1.2"/>')
    for k in range(1, 9):
        t = (k / 9) ** 2.2
        y = vy1 + (H - vy1) * t
        s.append(f'<line x1="0" y1="{y:.1f}" x2="{W}" y2="{y:.1f}" stroke="#3a3128" stroke-opacity=".25"/>')

    # storefront shutters on both walls
    def wall_pt(x, side):
        # returns top & bottom y on wall at screen x (left wall: 0..bx0)
        if side == "L":
            f = x / bx0
        else:
            f = (W - x) / (W - bx1)
        return vy0 * f, H - (H - vy1) * f

    shops = [(40, 170), (205, 300), (318, 380), (392, 430)]
    for side in "LR":
        for a, b in shops:
            if side == "R":
                a, b = W - b, W - a
            ta, ba = wall_pt(a, side)
            tb, bb = wall_pt(b, side)
            # shutter area: from 30% to 92% of wall height
            def lerp(t, u, f):
                return t + (u - t) * f
            ya0, ya1 = lerp(ta, ba, .28), lerp(ta, ba, .9)
            yb0, yb1 = lerp(tb, bb, .28), lerp(tb, bb, .9)
            s.append(f'<polygon points="{a},{ya0:.1f} {b},{yb0:.1f} {b},{yb1:.1f} {a},{ya1:.1f}" fill="#1f1b17" stroke="#2c2620" stroke-width="2"/>')
            for j in range(1, 14):
                f = j / 14
                s.append(f'<line x1="{a}" y1="{lerp(ya0, ya1, f):.1f}" x2="{b}" y2="{lerp(yb0, yb1, f):.1f}" stroke="#0e0c0a" stroke-opacity=".8" stroke-width="1.4"/>')
            # dead shop sign
            s.append(f'<polygon points="{a},{lerp(ta,ba,.14):.1f} {b},{lerp(tb,bb,.14):.1f} {b},{lerp(tb,bb,.23):.1f} {a},{lerp(ta,ba,.23):.1f}" fill="#191512"/>')
    # one flickering shop sign in amber on the right
    s.append('<polygon points="790,120 905,72 905,108 790,148" fill="#ffb347" opacity=".18" filter="url(#blur3)"/>')

    # ceiling lights converging (one off, one flickering)
    for k in range(7):
        t = 1 - (k / 7) ** 0.75
        y = vy0 * t + 6
        hw = 12 + 120 * t
        hh = 2 + 9 * t
        on = k not in (2, 5)
        op = 1 if on else .12
        if k == 4:
            op = .45
        s.append(f'<rect x="{512-hw:.1f}" y="{y-hh:.1f}" width="{2*hw:.1f}" height="{2*hh:.1f}" rx="2" fill="#f4ead2" opacity="{op}"/>')
        if on:
            s.append(f'<ellipse cx="512" cy="{y+hh*3:.1f}" rx="{hw*1.6:.1f}" ry="{hh*6:.1f}" fill="#f4dfb0" opacity="{.10*op:.2f}" filter="url(#blur8)"/>')
            # floor reflection
            fy = H - (y / vy0) * (H - vy1) if y < vy0 else vy1
            s.append(f'<ellipse cx="512" cy="{H - y*1.15 + 30:.1f}" rx="{hw*1.1:.1f}" ry="{hh*2.2:.1f}" fill="#f4dfb0" opacity="{.08*op:.2f}" filter="url(#blur8)"/>')

    # silhouette with eyes at the far end
    s.append(f'<path d="M500,{vy1} L500,236 Q500,222 512,220 Q524,222 524,236 L524,{vy1} Z" fill="#050404"/>')
    s.append('<circle cx="512" cy="214" r="9" fill="#050404"/>')
    for ex in (508, 516):
        s.append(f'<circle cx="{ex}" cy="213" r="9" fill="url(#eye)"/><circle cx="{ex}" cy="213" r="1.6" fill="#ffd2c4"/>')

    # fuel can foreground right
    cx, cy = 820, 360
    s.append(f'<ellipse cx="{cx}" cy="{cy+88}" rx="150" ry="40" fill="url(#canlight)"/>')
    s.append(f'<ellipse cx="{cx}" cy="{cy+92}" rx="74" ry="12" fill="#000" opacity=".6" filter="url(#blur3)"/>')
    s.append(f'<path d="M{cx-58},{cy-40} L{cx+40},{cy-40} L{cx+58},{cy-22} L{cx+58},{cy+86} Q{cx+58},{cy+92} {cx+52},{cy+92} L{cx-52},{cy+92} Q{cx-58},{cy+92} {cx-58},{cy+86} Z" fill="url(#can)" stroke="#2a0605" stroke-width="2"/>')
    s.append(f'<path d="M{cx-40},{cy-40} L{cx-40},{cy-66} Q{cx-40},{cy-72} {cx-34},{cy-72} L{cx+6},{cy-72} Q{cx+12},{cy-72} {cx+12},{cy-66} L{cx+12},{cy-40}" fill="none" stroke="#a81f17" stroke-width="12" stroke-linejoin="round"/>')
    s.append(f'<path d="M{cx+30},{cy-40} L{cx+44},{cy-80} L{cx+58},{cy-76} L{cx+48},{cy-38} Z" fill="#7a7468"/>')
    s.append(f'<path d="M{cx-44},{cy-16} L{cx+44},{cy+64} M{cx+44},{cy-16} L{cx-44},{cy+64}" stroke="#7d140f" stroke-width="7" opacity=".7"/>')
    s.append(f'<rect x="{cx-58}" y="{cy-40}" width="12" height="132" fill="#fff" opacity=".07"/>')

    # title
    s.append('<g font-family="Impact, \'Arial Black\', sans-serif" text-anchor="start">')
    s.append('<text x="58" y="402" font-size="84" fill="#b3170f" opacity=".55" filter="url(#blur8)" letter-spacing="4">HORROR MALL</text>')
    s.append('<text x="58" y="402" font-size="84" fill="#efe6d4" letter-spacing="4">HORROR MALL</text>')
    s.append('<text x="62" y="442" font-family="Bahnschrift, \'Segoe UI\', sans-serif" font-size="22" fill="#c9a87a" letter-spacing="7">FIND 12 FUEL CANS · ESCAPE</text>')
    s.append('</g>')
    s.append(f'<rect width="{W}" height="{H}" fill="url(#vig)"/>')
    s.append(f'<rect width="{W}" height="{H}" filter="url(#grain)"/>')
    s.append('</svg>')
    return "\n".join(s)


def toilet_survivor():
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">']
    s.append("""<defs>
<pattern id="tiles" width="44" height="44" patternUnits="userSpaceOnUse"><rect width="44" height="44" fill="#17403f"/><rect x="1.5" y="1.5" width="41" height="41" rx="3" fill="#1d4d4b"/><rect x="4" y="4" width="18" height="6" rx="3" fill="#2a6461" opacity=".55"/></pattern>
<pattern id="floor" width="60" height="60" patternUnits="userSpaceOnUse"><rect width="60" height="60" fill="#121616"/><rect width="30" height="30" fill="#1a1f1f"/><rect x="30" y="30" width="30" height="30" fill="#1a1f1f"/></pattern>
<linearGradient id="shade" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#000" stop-opacity=".55"/><stop offset=".45" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".7"/></linearGradient>
<radialGradient id="lamp" cx="50%" cy="0%" r="80%"><stop offset="0" stop-color="#d6fff6" stop-opacity=".28"/><stop offset="1" stop-color="#d6fff6" stop-opacity="0"/></radialGradient>
<radialGradient id="vig" cx="50%" cy="50%" r="72%"><stop offset=".55" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".8"/></radialGradient>
<radialGradient id="eye" r="50%"><stop offset="0" stop-color="#d9ff5a"/><stop offset=".4" stop-color="#8fd61a" stop-opacity=".8"/><stop offset="1" stop-color="#8fd61a" stop-opacity="0"/></radialGradient>
<radialGradient id="flash" r="50%"><stop offset="0" stop-color="#fff6c8"/><stop offset=".3" stop-color="#ffd36e" stop-opacity=".9"/><stop offset="1" stop-color="#ff8a00" stop-opacity="0"/></radialGradient>
<filter id="blur6"><feGaussianBlur stdDeviation="6"/></filter>
<filter id="grain"><feTurbulence type="fractalNoise" baseFrequency=".85" numOctaves="2" seed="9"/><feColorMatrix values="0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  0 0 0 .06 0"/></filter>
</defs>""")
    s.append(f'<rect width="{W}" height="360" fill="url(#tiles)"/>')
    s.append(f'<rect y="356" width="{W}" height="8" fill="#0d2423"/>')
    s.append(f'<polygon points="0,364 {W},364 {W},{H} 0,{H}" fill="url(#floor)"/>')
    s.append(f'<rect width="{W}" height="{H}" fill="url(#lamp)"/>')
    # stalls
    stalls = [(70, "closed"), (300, "ajar"), (530, "closed"), (760, "closed")]
    for x, st in stalls:
        w = 200
        s.append(f'<rect x="{x-8}" y="70" width="{w+16}" height="10" fill="#9aa7a6"/>')
        s.append(f'<rect x="{x-8}" y="70" width="10" height="290" fill="#7f8c8b"/>')
        if st == "ajar":
            s.append(f'<rect x="{x+2}" y="80" width="{w-2}" height="250" fill="#030606"/>')
            # glowing eyes inside
            for ex, ey in ((x+88, 170), (x+116, 170)):
                s.append(f'<circle cx="{ex}" cy="{ey}" r="14" fill="url(#eye)"/><circle cx="{ex}" cy="{ey}" r="2.4" fill="#f4ffd0"/>')
            s.append(f'<polygon points="{x+2},80 {x+70},96 {x+70},318 {x+2},330" fill="#4e6b69"/>')
            s.append(f'<polygon points="{x+2},80 {x+70},96 {x+70},318 {x+2},330" fill="#000" opacity=".25"/>')
        else:
            s.append(f'<rect x="{x+2}" y="80" width="{w-2}" height="250" fill="#5f7d7b"/>')
            s.append(f'<rect x="{x+12}" y="90" width="{w-22}" height="230" fill="#577573"/>')
            s.append(f'<rect x="{x+w-30}" y="196" width="14" height="22" rx="3" fill="#c9d4d2"/>')
            s.append(f'<rect x="{x+w-27}" y="200" width="8" height="5" fill="#c0392b"/>')
        # feet under doors (enemies waiting)
        if st == "closed" and x != 70:
            fx = x + 60
            s.append(f'<rect x="{fx}" y="340" width="30" height="16" rx="7" fill="#0b0f0f"/><rect x="{fx+52}" y="340" width="30" height="16" rx="7" fill="#0b0f0f"/>')
        s.append(f'<rect x="{x+w-2}" y="70" width="10" height="290" fill="#7f8c8b"/>')
    # shadow of the stall gap on floor
    s.append(f'<rect y="356" width="{W}" height="24" fill="#000" opacity=".35" filter="url(#blur6)"/>')
    s.append(f'<rect width="{W}" height="{H}" fill="url(#shade)"/>')
    # toilet paper roll foreground (barricade vibe)
    s.append('<g transform="translate(118 404)"><ellipse cx="0" cy="56" rx="64" ry="10" fill="#000" opacity=".5"/><rect x="-46" y="-40" width="92" height="96" rx="10" fill="#e9ecea"/><ellipse cx="0" cy="-40" rx="46" ry="14" fill="#f7f8f7"/><ellipse cx="0" cy="-40" rx="14" ry="5" fill="#8b8f8d"/><path d="M46,30 Q70,46 92,40 L92,60 Q66,64 46,52 Z" fill="#dfe3e1"/></g>')
    # crosshair + muzzle flash
    s.append('<g transform="translate(400 176)" stroke="#ffd36e" stroke-width="4" fill="none" opacity=".95"><circle r="40"/><line x1="-62" x2="-22"/><line x1="22" x2="62"/><line y1="-62" y2="-22"/><line y1="22" y2="62"/></g>')
    s.append('<circle cx="400" cy="176" r="4" fill="#ffd36e"/>')
    s.append('<circle cx="958" cy="430" r="90" fill="url(#flash)" opacity=".75"/>')
    # HUD chips
    s.append('<g font-family="Bahnschrift, \'Segoe UI\', sans-serif" font-weight="700">')
    s.append('<rect x="36" y="24" width="150" height="40" rx="20" fill="#000" opacity=".6"/><text x="111" y="51" font-size="20" fill="#ffd36e" text-anchor="middle" letter-spacing="3">WAVE 07</text>')
    s.append('<rect x="198" y="24" width="150" height="40" rx="20" fill="#000" opacity=".6"/><text x="273" y="51" font-size="20" fill="#9ff2e4" text-anchor="middle" letter-spacing="3">2 PLAYERS</text>')
    s.append('</g>')
    # title
    s.append('<g font-family="Impact, \'Arial Black\', sans-serif" text-anchor="end">')
    s.append('<text x="986" y="420" font-size="78" fill="#000" stroke="#000" stroke-width="14" stroke-linejoin="round" letter-spacing="2">TOILET SURVIVOR</text>')
    s.append('<text x="986" y="420" font-size="78" fill="#ffd36e" letter-spacing="2">TOILET SURVIVOR</text>')
    s.append('<text x="984" y="458" font-family="Bahnschrift, \'Segoe UI\', sans-serif" font-size="21" fill="#d6f5ef" letter-spacing="6">HOLD THE LINE · WAVE AFTER WAVE</text>')
    s.append('</g>')
    s.append(f'<rect width="{W}" height="{H}" fill="url(#vig)"/>')
    s.append(f'<rect width="{W}" height="{H}" filter="url(#grain)"/>')
    s.append('</svg>')
    return "\n".join(s)


(OUT / "horror-mall.svg").write_text(horror_mall(), encoding="utf-8")
(OUT / "toilet-survivor.svg").write_text(toilet_survivor(), encoding="utf-8")
print("ok")
