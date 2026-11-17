"""Builds the Ink & Quill (INQEDU) site into ./site.

Run:  python3 build.py
Edit the page text below, or add a guide to GUIDES, then run again.
The header and footer are defined once here so every page stays in step.
"""
from pathlib import Path

OUT = Path(__file__).parent / "site"
BRAND = "Ink &amp; Quill"

NAV = [("Home", "index.html"), ("Classes", "classes.html"), ("Guides", "guides.html"), ("Contact", "contact.html")]


def page(path, title, description, body, current, root=""):
    links = "".join(
        f'<a href="{root}{href}"{" aria-current=\"page\"" if href == current else ""}>{name}</a>'
        for name, href in NAV
    )
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="icon" href="{root}assets/favicon.png">
<link rel="stylesheet" href="{root}css/styles.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <div class="wrap">
    <a class="brand" href="{root}index.html" aria-label="Ink and Quill home">
      <img src="{root}assets/mark.png" alt="" width="61" height="50">
      <span class="brand-name">{BRAND}<small>IB Tuition</small></span>
    </a>
    <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="site-nav">Menu</button>
    <nav class="nav" id="site-nav" aria-label="Main">
      {links}
      <a class="btn" href="{root}contact.html">Enquire</a>
    </nav>
  </div>
</header>
<main id="main">
{body}
</main>
<footer class="site-footer">
  <div class="wrap">
    <div class="top">
      <div>
        <img class="logo" src="{root}assets/logo.png" alt="Ink and Quill" width="820" height="392">
        <p class="measure">IB Diploma tuition, specialising in English A: Language &amp; Literature and Literature.</p>
      </div>
      <div>
        <p class="label">Explore</p>
        <ul>
          <li><a href="{root}classes.html">Subjects and classes</a></li>
          <li><a href="{root}guides.html">Guides and blog</a></li>
          <li><a href="{root}contact.html">Contact</a></li>
        </ul>
      </div>
      <div>
        <p class="label">Get in touch</p>
        <ul>
          <li><a href="{root}contact.html">Send an enquiry</a></li>
          <li class="todo">Email: to be added</li>
          <li class="todo">WhatsApp: to be added</li>
        </ul>
      </div>
    </div>
    <div class="bottom">
      <span>&copy; 2026 Ink &amp; Quill (INQEDU)</span>
      <span>Singapore</span>
    </div>
  </div>
</footer>
<script src="{root}js/main.js"></script>
</body>
</html>
"""
    target = OUT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(html, encoding="utf-8")


def cta(root=""):
    return f"""<section class="cta">
  <div class="wrap">
    <div>
      <span class="label">Enquiries</span>
      <h2>Curious what a lesson is like?</h2>
      <p>Tell us which subjects you take and where you feel stuck. We will reply with class times and the next step.</p>
    </div>
    <a class="btn btn--light" href="{root}contact.html">Send an enquiry</a>
  </div>
</section>"""


# ---------------------------------------------------------------- Guides
GUIDES = [
    {
        "slug": "paper-1-unseen-text",
        "kind": "Guide",
        "minutes": 4,
        "title": "Paper 1: a method for the unseen text",
        "summary": "What to do in the first ten minutes with a text you have never seen, so the essay has an argument before you start writing.",
        "body": """
<p>Paper 1 gives you a text you have never read and a guiding question. Standard Level students write on one text. Higher Level students write on two. Most weak scripts fail in the same way: they walk through the text from top to bottom and name techniques as they pass. A strong script decides what the text is doing first, then proves it.</p>
<h2>1. Read for the situation before the style</h2>
<p>On the first read, leave your pen down. Ask four plain questions. Who is speaking? To whom? About what? What does the writer want the reader to think, feel or do by the end? If you cannot answer the last one in a sentence, read again. Everything else in your essay hangs on it.</p>
<h2>2. Find the turn</h2>
<p>Almost every passage shifts somewhere. The tone hardens, the focus narrows, the speaker changes their mind, an advertisement moves from problem to product. Mark that point. It usually gives you your structure: what the text does before the turn, what it does after, and why the change matters.</p>
<h2>3. Choose three or four features that carry the meaning</h2>
<p>You are not paid per technique. Pick the features that do the most work for the purpose you identified in step one. For a non-literary text this may include layout, image and typography as well as language. For each one, be ready to say what it is, where it appears, and what it makes the reader think.</p>
<h2>4. Write a thesis that answers the guiding question</h2>
<p>The guiding question is there to help you. Use its key words. A workable thesis has two parts: what the text achieves, and the main ways it achieves it.</p>
<blockquote>The writer presents the city as a place that has already claimed its people, using repetition and a speaker who can only observe.</blockquote>
<h2>5. Plan paragraphs around ideas</h2>
<p>Each paragraph should argue one point about the text's meaning. Avoid paragraphs titled by device, such as a paragraph on imagery followed by a paragraph on tone. Organise by what the text is doing, and bring in whichever features prove it.</p>
<h2>A note on time</h2>
<p>Ten minutes of planning feels expensive in the exam room. It is the cheapest marks you will earn. An essay with a clear line of argument and three well-developed points will outscore a longer one that describes.</p>
""",
    },
    {
        "slug": "individual-oral-global-issue",
        "kind": "Guide",
        "minutes": 4,
        "title": "Choosing a global issue for your Individual Oral",
        "summary": "A good global issue is narrow enough to argue and visible in the actual words of both your texts. Here is how to test yours.",
        "body": """
<p>The Individual Oral asks you to examine how two of the works you have studied present a global issue of your choice. You speak for ten minutes and then answer questions from your teacher for five. The choice of issue decides how well those ten minutes go, and most students choose one that is far too wide.</p>
<h2>Too wide, too narrow, about right</h2>
<p>"Gender inequality" is a topic. You could speak about it for an hour without saying anything about your texts. A global issue needs to be specific enough that your two texts take a position on it.</p>
<ul>
<li><strong>Too wide:</strong> gender inequality.</li>
<li><strong>About right:</strong> how domestic expectations limit women's ability to speak for themselves.</li>
<li><strong>Too narrow:</strong> the treatment of one character in one scene.</li>
</ul>
<h2>Three tests</h2>
<ol>
<li><strong>Is it significant and felt in many places?</strong> The issue should matter beyond one country or one decade, and show up in everyday life.</li>
<li><strong>Can you point to it in the language?</strong> Open each extract. If you cannot underline the lines where the issue is present, the link is in your head and not in the text.</li>
<li><strong>Do the two texts treat it differently?</strong> The oral is more interesting, and easier to structure, when the texts approach the issue from different angles or through different forms.</li>
</ol>
<h2>Choose the extracts for what they let you analyse</h2>
<p>Your extracts should be rich in choices you can discuss: imagery, structure, voice, or visual features in a non-literary text. A passage that states the issue outright often gives you less to say than one that shows it indirectly.</p>
<h2>Give both texts equal weight</h2>
<p>Split your time evenly. For each text, move between the extract and the wider work, so the examiner can see you know the whole and not only the lines in front of you.</p>
<h2>Practise aloud</h2>
<p>An oral is a spoken argument. Record yourself, listen back, and note where you describe instead of analyse. Do this at least twice before the real thing. Your notes should be prompts, never a script.</p>
""",
    },
    {
        "slug": "technique-to-analysis",
        "kind": "Guide",
        "minutes": 3,
        "title": "From spotting techniques to analysing them",
        "summary": "Naming a metaphor earns very little. This is the three-step habit that turns an observation into analysis.",
        "body": """
<p>Teachers write "analyse, don't describe" in the margin more than any other comment. It is hard to act on because description and analysis can look similar. The difference is what the sentence does after it names the feature.</p>
<h2>What description looks like</h2>
<blockquote>Blake uses repetition in the word "charter'd" to emphasise it.</blockquote>
<p>This is true and it says almost nothing. Every repetition emphasises. The sentence could be written about any repeated word in any text.</p>
<h2>The three steps</h2>
<ol>
<li><strong>Choice.</strong> What exactly did the writer choose? Quote the smallest piece that carries the effect.</li>
<li><strong>Effect.</strong> What does that choice make a reader notice, picture or feel? Be specific to these words.</li>
<li><strong>Meaning.</strong> How does that effect serve the larger idea of the text, and your argument about it?</li>
</ol>
<h2>What analysis looks like</h2>
<blockquote>Blake applies "charter'd" first to a street and then to the Thames. A street can be owned, but a river is a natural thing, so the second use is unsettling. The repetition suggests that in this London even nature has been mapped and claimed, which prepares us for a poem where people, too, are marked and held.</blockquote>
<p>The feature is the same. The second version explains why this word matters in this poem, and ties it to an argument.</p>
<h2>A quick self-check</h2>
<p>After every sentence that names a technique, ask "so what?" If your next sentence answers that question, you are analysing. If it moves on to another technique, go back.</p>
""",
    },
]


def guide_cards(root=""):
    cards = []
    for g in GUIDES:
        cards.append(f"""<a class="card card-link post-card" href="{root}guides/{g['slug']}.html">
        <p class="meta"><span>{g['kind']}</span><span>{g['minutes']} min read</span></p>
        <h3>{g['title']}</h3>
        <p>{g['summary']}</p>
      </a>""")
    return "\n      ".join(cards)


# ------------------------------------------------------------------ Home
home = f"""<section class="hero">
  <div class="wrap">
    <div class="hero-copy">
      <p class="label">IB Diploma tuition &middot; Specialists in English A</p>
      <h1>Read like a writer. <em>Write like a critic.</em></h1>
      <p class="lede">Ink &amp; Quill is an IB tuition centre that specialises in English A: Language &amp; Literature and Literature. Our classes are interactive and discussion-led, and we also teach History, Geography, Business Management and both Mathematics courses.</p>
      <div class="actions">
        <a class="btn" href="contact.html">Send an enquiry</a>
        <a class="btn btn--ghost" href="classes.html">See the classes</a>
      </div>
    </div>
    <figure class="reading" aria-label="An annotated passage">
      <span class="label">A close reading</span>
      <blockquote class="poem">
        <span class="line">I wander thro' each <mark data-n="1">charter'd</mark> street,</span>
        <span class="line">Near where the <mark data-n="1">charter'd</mark> Thames does flow.</span>
        <span class="line">And <mark data-n="2">mark</mark> in <mark data-n="3">every</mark> face I meet</span>
        <span class="line"><mark data-n="2">Marks</mark> of weakness, <mark data-n="2">marks</mark> of woe.</span>
      </blockquote>
      <ol class="notes">
        <li data-n="1" tabindex="0"><span><strong>charter'd, twice.</strong> A street can be owned. A river should not be. Repeating the word makes ownership feel total.</span></li>
        <li data-n="2" tabindex="0"><span><strong>mark, then Marks.</strong> A verb becomes a noun. The speaker looks, and what he sees is damage already done.</span></li>
        <li data-n="3" tabindex="0"><span><strong>every.</strong> No face is spared. Watch this word return through the rest of the poem.</span></li>
      </ol>
      <p class="source">William Blake, &ldquo;London&rdquo; (1794), lines 1&ndash;4</p>
    </figure>
  </div>
</section>

<section class="band band--linen">
  <div class="wrap cols">
    <p class="label">Subjects</p>
    <div>
      <div class="band-head">
        <h2>Specialists in IB English, with five more subjects</h2>
        <p class="measure">Every class follows the IB Diploma syllabus, at Standard and Higher Level.</p>
      </div>
      <p class="label" style="margin-bottom: 1rem;">Our specialism</p>
      <div class="grid-2">
        <article class="card">
          <div class="levels"><span class="pill">SL</span><span class="pill">HL</span></div>
          <h3>English A: Language &amp; Literature</h3>
          <p>Literary works alongside the texts of everyday life: advertisements, speeches, opinion columns and cartoons. You learn to explain how any text shapes its audience.</p>
          <a class="more" href="classes.html#language-and-literature">Course details</a>
        </article>
        <article class="card">
          <div class="levels"><span class="pill">SL</span><span class="pill">HL</span></div>
          <h3>English A: Literature</h3>
          <p>Poetry, prose, drama and works in translation. You build the close-reading habits and the critical vocabulary that the course rewards.</p>
          <a class="more" href="classes.html#literature">Course details</a>
        </article>
      </div>
      <p class="label" style="margin: 2.6rem 0 1rem;">Also taught</p>
      <ul class="also">
        <li><a href="classes.html#history">History</a><span>SL &middot; HL</span></li>
        <li><a href="classes.html#geography">Geography</a><span>SL &middot; HL</span></li>
        <li><a href="classes.html#business">Business Management</a><span>SL &middot; HL</span></li>
        <li><a href="classes.html#maths-aa">Mathematics: Analysis &amp; Approaches</a><span>SL &middot; HL</span></li>
        <li><a href="classes.html#maths-ai">Mathematics: Applications &amp; Interpretation</a><span>SL &middot; HL</span></li>
      </ul>
      <p style="margin-top: 2.2rem;"><a class="more" href="classes.html">All subjects and class details</a></p>
    </div>
  </div>
</section>

<section class="band">
  <div class="wrap cols">
    <p class="label">In the classroom</p>
    <div>
      <div class="band-head">
        <h2>Unlike the lessons you have sat through before</h2>
      </div>
      <div class="principles">
        <div>
          <h3>You do the talking</h3>
          <p>Every lesson is built around discussion. You test your reading against other people's and learn to defend it.</p>
        </div>
        <div>
          <h3>A new way into the subject</h3>
          <p>We start from how each subject thinks: how a writer, a historian or a mathematician builds an argument. Then you learn to make that argument yourself.</p>
        </div>
        <div>
          <h3>Tutors who know the course</h3>
          <p>Experienced tutors lead every class and show you what each assessment is really asking for.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="band band--linen">
  <div class="wrap cols">
    <p class="label">English A</p>
    <div>
      <div class="band-head">
        <h2>Every English A component, prepared for</h2>
      </div>
      <ul class="ruled">
        <li><h3>Paper 1</h3><p>Guided analysis of texts you have not seen before, written under timed conditions.</p></li>
        <li><h3>Paper 2</h3><p>A comparative essay on two of the works you have studied, in response to a set question.</p></li>
        <li><h3>Individual Oral</h3><p>A fifteen-minute oral that examines how two works present a global issue of your choice.</p></li>
        <li><h3>HL Essay<span class="note">Higher Level only</span></h3><p>A formal essay of 1,200 to 1,500 words that develops your own line of inquiry into one work.</p></li>
      </ul>
    </div>
  </div>
</section>

<section class="band">
  <div class="wrap cols">
    <p class="label">Guides</p>
    <div>
      <div class="band-head">
        <h2>Free guides for IB English students</h2>
      </div>
      <div class="grid-3">
      {guide_cards()}
      </div>
      <p style="margin-top: 2.2rem;"><a class="more" href="guides.html">All guides and blog posts</a></p>
    </div>
  </div>
</section>

{cta()}"""

page("index.html", "Ink &amp; Quill IB Tuition",
     "IB Diploma tuition specialising in English A Language and Literature and Literature, plus History, Geography, Business Management and Mathematics.",
     home, "index.html")

# --------------------------------------------------------------- Classes
classes = f"""<section class="page-head">
  <div class="wrap">
    <p class="label">Classes</p>
    <h1>IB Diploma subjects, <em>Standard and Higher Level</em></h1>
    <p class="lede">We specialise in both English A courses, and also teach History, Geography, Business Management and Mathematics. Classes are interactive: you discuss, practise, and get feedback you can act on.</p>
  </div>
</section>

<section class="band band--linen">
  <div class="wrap cols">
    <p class="label">Our specialism</p>
    <div>
      <div class="band-head">
        <h2>English A</h2>
        <p class="measure">Our tutors specialise in both English A courses. This is where our approach to reading and argument began.</p>
      </div>
      <article class="course" id="language-and-literature">
        <div class="stack">
          <div class="levels"><span class="pill">SL</span><span class="pill">HL</span></div>
          <h2>English A: Language &amp; Literature</h2>
          <p>This course pairs literary works with non-literary texts. One week you may study a novel, the next a political speech or an advertising campaign. The skill underneath is the same: explaining how a text is constructed to affect its audience.</p>
        </div>
        <ul aria-label="What we work on">
          <li>Analysing non-literary text types: advertisements, speeches, articles, cartoons, websites</li>
          <li>Reading for audience, purpose and context</li>
          <li>Commenting on visual and structural features as well as language</li>
          <li>Linking literary works and non-literary texts to a global issue for the Individual Oral</li>
          <li>Planning and writing Paper 1 and Paper 2 under timed conditions</li>
        </ul>
      </article>
      <article class="course" id="literature">
        <div class="stack">
          <div class="levels"><span class="pill">SL</span><span class="pill">HL</span></div>
          <h2>English A: Literature</h2>
          <p>This course is the close study of literary works across poetry, prose, drama and literature in translation. It rewards students who can read slowly, notice precisely, and build an interpretation that is their own.</p>
        </div>
        <ul aria-label="What we work on">
          <li>Close reading of unseen poetry and prose</li>
          <li>Understanding form, structure and voice in each literary genre</li>
          <li>Comparing works for Paper 2 without retelling the plot</li>
          <li>Choosing extracts and a global issue for the Individual Oral</li>
          <li>Developing a line of inquiry for the HL Essay</li>
        </ul>
      </article>
    </div>
  </div>
</section>

<section class="band">
  <div class="wrap cols">
    <p class="label">English A assessments</p>
    <div>
      <div class="band-head">
        <h2>What English A students are assessed on</h2>
        <p class="measure">Both English A courses share the same assessment structure. Our lessons work through every component.</p>
      </div>
      <div class="table-wrap">
        <table>
          <thead>
            <tr><th scope="col">Component</th><th scope="col">What it is</th><th scope="col">Standard Level</th><th scope="col">Higher Level</th></tr>
          </thead>
          <tbody>
            <tr><th scope="row">Paper 1</th><td>Guided analysis of unseen texts</td><td>One text, 1 h 15 min, 35%</td><td>Two texts, 2 h 15 min, 35%</td></tr>
            <tr><th scope="row">Paper 2</th><td>Comparative essay on two works studied</td><td>1 h 45 min, 35%</td><td>1 h 45 min, 25%</td></tr>
            <tr><th scope="row">Individual Oral</th><td>Fifteen-minute oral on a global issue</td><td>30%</td><td>20%</td></tr>
            <tr><th scope="row">HL Essay</th><td>Essay of 1,200 to 1,500 words</td><td>Not required</td><td>20%</td></tr>
          </tbody>
        </table>
      </div>
      <p class="small" style="margin-top: 1.2rem;">Timings and weightings follow the current IB English A subject guides. Your school will confirm the details for your exam session.</p>
    </div>
  </div>
</section>

<section class="band band--linen">
  <div class="wrap cols">
    <p class="label">Also offered</p>
    <div>
      <div class="band-head">
        <h2>Humanities, business and mathematics</h2>
        <p class="measure">The same interactive approach, applied to five more IB Diploma subjects.</p>
      </div>
      <div class="grid-3">
        <article class="card subject" id="history">
          <div class="levels"><span class="pill">SL</span><span class="pill">HL</span></div>
          <h3>History</h3>
          <p>Source analysis, essay planning and historical argument across your prescribed subject and world history topics. HL students also prepare their regional option.</p>
        </article>
        <article class="card subject" id="geography">
          <div class="levels"><span class="pill">SL</span><span class="pill">HL</span></div>
          <h3>Geography</h3>
          <p>Core and optional themes, data and map interpretation, and the extended responses that the exam papers reward.</p>
        </article>
        <article class="card subject" id="business">
          <div class="levels"><span class="pill">SL</span><span class="pill">HL</span></div>
          <h3>Business Management</h3>
          <p>Business concepts and tools applied to real organisations, with practice on case studies and structured exam questions.</p>
        </article>
        <article class="card subject" id="maths-aa">
          <div class="levels"><span class="pill">SL</span><span class="pill">HL</span></div>
          <h3>Mathematics: Analysis &amp; Approaches</h3>
          <p>Algebra, functions, calculus and proof, for students who enjoy abstract reasoning. Includes guidance on the mathematical exploration.</p>
        </article>
        <article class="card subject" id="maths-ai">
          <div class="levels"><span class="pill">SL</span><span class="pill">HL</span></div>
          <h3>Mathematics: Applications &amp; Interpretation</h3>
          <p>Statistics, modelling and technology-assisted problem solving in real-world contexts. Includes guidance on the mathematical exploration.</p>
        </article>
      </div>
    </div>
  </div>
</section>

<section class="band">
  <div class="wrap cols">
    <p class="label">Joining</p>
    <div class="stack">
      <h2>Class times and fees</h2>
      <p class="measure">Send us an enquiry with your subjects, levels and year of study. We will reply with the current timetable, fees and how to join a class.</p>
      <div class="actions" style="margin-top: 0.6rem;"><a class="btn" href="contact.html">Send an enquiry</a></div>
    </div>
  </div>
</section>"""

page("classes.html", "Subjects and Classes at Ink &amp; Quill",
     "IB Diploma classes in English A Language and Literature, Literature, History, Geography, Business Management and Mathematics, at Standard and Higher Level.",
     classes, "classes.html")

# ---------------------------------------------------------------- Guides
guides = f"""<section class="page-head">
  <div class="wrap">
    <p class="label">Guides and blog</p>
    <h1>Read better. <em>Write better.</em></h1>
    <p class="lede">Practical guides to IB English from our tutors. They are free to read and written to be used the night before a deadline.</p>
  </div>
</section>

<section class="band band--linen">
  <div class="wrap">
    <div class="grid-3">
      {guide_cards()}
    </div>
  </div>
</section>

{cta()}"""

page("guides.html", "Ink &amp; Quill Guides and Blog",
     "Free guides to IB English Language and Literature and Literature: Paper 1, Paper 2, the Individual Oral and the HL Essay.",
     guides, "guides.html")

for g in GUIDES:
    article = f"""<article class="article">
  <header>
    <p class="meta"><span>{g['kind']}</span><span>{g['minutes']} min read</span></p>
    <h1>{g['title']}</h1>
    <p class="lede">{g['summary']}</p>
  </header>
  <div class="prose">{g['body']}</div>
  <footer>
    <a class="more" href="../guides.html">All guides</a>
    <a class="btn" href="../contact.html">Ask about classes</a>
  </footer>
</article>"""
    page(f"guides/{g['slug']}.html", f"{g['title']} | Ink &amp; Quill", g["summary"], article, "guides.html", root="../")

# --------------------------------------------------------------- Contact
contact = """<section class="page-head">
  <div class="wrap">
    <p class="label">Contact</p>
    <h1>Send us <em>an enquiry</em></h1>
    <p class="lede">Tell us a little about the student, which subjects they take, and what they need help with. We will reply with class times and the next step.</p>
  </div>
</section>

<section class="band band--linen">
  <div class="wrap contact">
    <form id="enquiry-form" novalidate-off>
      <div class="field">
        <label for="name">Your name</label>
        <input id="name" name="name" type="text" autocomplete="name" required>
      </div>
      <div class="field">
        <label for="email">Email</label>
        <input id="email" name="email" type="email" autocomplete="email" required>
      </div>
      <div class="field">
        <label for="phone">Phone or WhatsApp <span class="opt">(optional)</span></label>
        <input id="phone" name="phone" type="tel" autocomplete="tel">
      </div>
      <div class="field">
        <label for="role">I am a</label>
        <select id="role" name="role">
          <option>Student</option>
          <option>Parent or guardian</option>
        </select>
      </div>
      <div class="field">
        <label for="course">Subject</label>
        <select id="course" name="subject" required>
          <option value="">Choose a subject</option>
          <option>English A: Language &amp; Literature</option>
          <option>English A: Literature</option>
          <option>History</option>
          <option>Geography</option>
          <option>Business Management</option>
          <option>Mathematics: Analysis &amp; Approaches</option>
          <option>Mathematics: Applications &amp; Interpretation</option>
          <option>More than one subject</option>
        </select>
      </div>
      <div class="field">
        <label for="level">Level</label>
        <select id="level" name="level">
          <option>Standard Level</option>
          <option>Higher Level</option>
          <option>Not sure yet</option>
        </select>
      </div>
      <div class="field field--full">
        <label for="message">How can we help?</label>
        <textarea id="message" name="message" required></textarea>
      </div>
      <div class="field field--full">
        <button class="btn" type="submit" style="justify-self: start; align-self: flex-start;">Send enquiry</button>
      </div>
      <p class="form-status" id="form-status" role="status" tabindex="-1" hidden></p>
    </form>
    <aside class="stack">
      <h2 style="font-size: 1.5rem;">Other ways to reach us</h2>
      <dl class="details">
        <div><dt>Email</dt><dd class="todo">To be added</dd></div>
        <div><dt>WhatsApp</dt><dd class="todo">To be added</dd></div>
        <div><dt>Location</dt><dd class="todo">To be added</dd></div>
      </dl>
    </aside>
  </div>
</section>""".replace(" novalidate-off", "")

page("contact.html", "Contact Ink &amp; Quill",
     "Send an enquiry about IB tuition at Ink and Quill.",
     contact, "contact.html")

print("Built", len(list(OUT.rglob("*.html"))), "pages into", OUT)
