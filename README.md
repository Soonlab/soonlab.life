# soonlab.life

Website of the Translational Bioinformatics Lab, Division of AI Data Science,
The University of Suwon (PI: Soon-Chan Kim).

## Layout

    index.html        the whole site (single page, anchor-linked sections)
    img/              graphical abstracts, one per research theme
    fonts/            self-hosted Newsreader + IBM Plex Mono (latin, latin-ext)
    favicon.svg  robots.txt  sitemap.xml

No build step and no external requests: the page is plain HTML/CSS/JS and every
asset is served from this directory.

## Editing

Edit `index.html` directly. Section order follows the nav: Our Goal, People,
Publications, Photos, Join Us, Contact.

The graphical abstracts under `img/` are generated from `ga/ga.html`
(rendered to PNG through headless Chromium); the two journal-style abstracts
(`ga_dp.jpg`, `ga_up.jpg`) come from the manuscripts themselves.

## Local preview

    python3 -m http.server 8899      # then open http://localhost:8899

## Deploy

Cloudflare Pages, project `soonlab`, custom domain `soonlab.life`.

    npx wrangler pages deploy . --project-name=soonlab
