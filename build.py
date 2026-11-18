"""Builds the Ink & Quill (INQEDU) site into ./site.

Run:  python3 build.py
Edit the page text below, or add a guide to GUIDES, then run again.
The header and footer are defined once here so every page stays in step.
"""
from pathlib import Path

from subjects import GROUPS, SUBJECTS

OUT = Path(__file__).parent / "site"
BRAND = "Ink &amp; Quill"

from urllib.parse import quote

WHATSAPP = "6588665396"
WHATSAPP_DISPLAY = "+65 8866 5396"
EMAIL = "admin@inqedu.com"


def whatsapp_link(subject=None):
    """wa.me link that opens WhatsApp with an enquiry message ready to send."""
    if subject:
        plain = subject.replace("&amp;", "&")
        text = (f"Hi Ink & Quill! I'd like to find out more about your IB {plain} classes.\n\n"
                "Student's name:\nSchool and year of study:\nLevel (SL or HL):")
    else:
        text = ("Hi Ink & Quill! I'd like to find out more about your IB classes.\n\n"
                "Student's name:\nSchool and year of study:\nSubject(s) and level (SL or HL):")
    return f"https://wa.me/{WHATSAPP}?text={quote(text)}"


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
        <p class="measure">IB Diploma tuition in seven subjects, at Standard and Higher Level.</p>
      </div>
      <div>
        <p class="label">Explore</p>
        <ul>
          <li><a href="{root}classes.html">Subjects and classes</a></li>
          <li><a href="{root}guides.html">Guides and blog</a></li>
          <li><a href="{root}contact.html#faq">Questions and answers</a></li>
          <li><a href="{root}contact.html">Contact</a></li>
        </ul>
      </div>
      <div>
        <p class="label">Get in touch</p>
        <ul>
          <li><a href="{root}contact.html">Send an enquiry</a></li>
          <li><a href="mailto:admin@inqedu.com">admin@inqedu.com</a></li>
          <li><a href="{whatsapp_link()}">WhatsApp {WHATSAPP_DISPLAY}</a></li>
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



# --------------------------------------------------------------- Subjects
def group_subjects(gid):
    return [x for x in SUBJECTS if x["group"] == gid]


def pills():
    return '<div class="levels"><span class="pill">SL</span><span class="pill">HL</span></div>'


def home_subjects():
    cols = []
    for gid, num, gname in GROUPS:
        items = "".join(
            f'<li><a href="classes/{x["slug"]}.html">{x["name"]}</a><span>SL &middot; HL</span></li>'
            for x in group_subjects(gid))
        cols.append(f'<div><p class="group-label"><span>{num}</span>{gname}</p><ul class="also">{items}</ul></div>')
    return f"""<section class="band band--linen">
  <div class="wrap cols">
    <p class="label">Subjects</p>
    <div>
      <div class="band-head">
        <h2>Seven IB Diploma subjects, at Standard and Higher Level</h2>
        <p class="measure">Every class follows the IB Diploma syllabus. Choose a subject to see what we cover, how it is assessed and when classes run.</p>
      </div>
      <div class="groups">{"".join(cols)}</div>
      <p style="margin-top: 2.2rem;"><a class="more" href="classes.html">All subjects and classes</a></p>
    </div>
  </div>
</section>"""


def subject_cards(root=""):
    out = []
    for gid, num, gname in GROUPS:
        cards = "".join(f"""
        <a class="card card-link subject-card" href="{root}classes/{x['slug']}.html">
          {pills()}
          <h3>{x['name']}</h3>
          <p>{x['short']}</p>
          <span class="more">View subject</span>
        </a>""" for x in group_subjects(gid))
        out.append(f"""<div class="group">
      <p class="group-label"><span>{num}</span>{gname}</p>
      <div class="grid-3">{cards}
      </div>
    </div>""")
    return "\n    ".join(out)


def slots_html(x):
    if not x["slots"]:
        return """<div class="slots-empty">
          <p><strong>Class times for this subject will be posted here soon.</strong></p>
          <p>Message us on WhatsApp and we will tell you the current timetable and whether places are available.</p>
        </div>"""
    rows = "".join(
        f"<tr><th scope=\"row\">{sl.get('level', '')}</th><td>{sl.get('day', '')}</td><td>{sl.get('time', '')}</td>"
        f"<td>{sl.get('format', '')}</td><td><span class=\"status\">{sl.get('status', '')}</span></td></tr>"
        for sl in x["slots"])
    return f"""<div class="table-wrap">
          <table>
            <thead><tr><th scope="col">Level</th><th scope="col">Day</th><th scope="col">Time</th><th scope="col">Format</th><th scope="col">Places</th></tr></thead>
            <tbody>{rows}</tbody>
          </table>
        </div>"""


def subject_page(x):
    group = next(g for g in GROUPS if g[0] == x["group"])
    cover = "".join(f"<li>{c}</li>" for c in x["cover"])
    rows = "".join(
        f'<tr><th scope="row">{c}</th><td>{w}</td><td>{sl}</td><td>{hl}</td></tr>'
        for c, w, sl, hl in x["assessment"])
    return f"""<section class="page-head">
  <div class="wrap">
    <p class="label"><a href="../classes.html">Classes</a> &nbsp;/&nbsp; {group[1]}: {group[2]}</p>
    <h1>{x['name']}</h1>
    {pills()}
    <p class="lede">{x['intro']}</p>
    <div class="actions"><a class="btn" href="{whatsapp_link(x['name'])}">Enquire on WhatsApp</a><a class="btn btn--ghost" href="#slots">See class slots</a></div>
  </div>
</section>

<section class="band band--linen">
  <div class="wrap cols">
    <p class="label">What we cover</p>
    <div>
      <ul class="checklist">{cover}</ul>
    </div>
  </div>
</section>

<section class="band">
  <div class="wrap cols">
    <p class="label">Assessment</p>
    <div>
      <div class="band-head">
        <h2>How {x['name']} is assessed</h2>
      </div>
      <div class="table-wrap">
        <table>
          <thead><tr><th scope="col">Component</th><th scope="col">What it is</th><th scope="col">Standard Level</th><th scope="col">Higher Level</th></tr></thead>
          <tbody>{rows}</tbody>
        </table>
      </div>
      <p class="small" style="margin-top: 1.2rem;">{x['note']}</p>
    </div>
  </div>
</section>

<section class="band band--linen" id="slots">
  <div class="wrap cols">
    <p class="label">Class slots</p>
    <div>
      <div class="band-head">
        <h2>When classes run</h2>
      </div>
      {slots_html(x)}
      <div class="actions" style="margin-top: 1.6rem;"><a class="btn" href="{whatsapp_link(x['name'])}">Enquire on WhatsApp</a></div>
    </div>
  </div>
</section>

<section class="band">
  <div class="wrap">
    <a class="more" href="../classes.html">All subjects</a>
  </div>
</section>"""

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

{home_subjects()}

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
    <p class="label">Guides</p>
    <div>
      <div class="band-head">
        <h2>Free guides for IB students</h2>
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
     "IB Diploma tuition in English A Language and Literature, Literature, History, Geography, Business Management and Mathematics, at SL and HL.",
     home, "index.html")

# --------------------------------------------------------------- Classes
classes = f"""<section class="page-head">
  <div class="wrap">
    <p class="label">Classes</p>
    <h1>IB Diploma subjects, <em>Standard and Higher Level</em></h1>
    <p class="lede">We teach seven IB Diploma subjects across three subject groups. Classes are interactive: you discuss, practise, and get feedback you can act on. Choose a subject to see what we cover, how it is assessed and when classes run.</p>
  </div>
</section>

<section class="band band--linen">
  <div class="wrap subject-groups">
    {subject_cards()}
  </div>
</section>

<section class="band">
  <div class="wrap cols">
    <p class="label">Joining</p>
    <div class="stack">
      <h2>Class times and fees</h2>
      <p class="measure">Each subject page lists its class slots. For fees, or a time that is not listed, send us an enquiry with your subjects, levels and year of study.</p>
      <div class="actions" style="margin-top: 0.6rem;"><a class="btn" href="contact.html">Send an enquiry</a></div>
    </div>
  </div>
</section>"""

page("classes.html", "Subjects and Classes at Ink &amp; Quill",
     "IB Diploma classes in English A Language and Literature, Literature, History, Geography, Business Management and Mathematics, at Standard and Higher Level.",
     classes, "classes.html")

for x in SUBJECTS:
    plain = x["name"].replace("&amp;", "and")
    page(f"classes/{x['slug']}.html", f"IB {x['name']} | Ink &amp; Quill",
         f"IB {plain} tuition at Ink and Quill: what we cover, how it is assessed, and class slots.",
         subject_page(x), "classes.html", root="../")

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

# -------------------------------------------------------------------- FAQ
FAQS = [
    ("Subjects and courses", [
        ("Which subjects do you teach?",
         '<p>We teach seven IB Diploma subjects: English A: Language &amp; Literature, English A: Literature, History, Geography, Business Management, Mathematics: Analysis &amp; Approaches, and Mathematics: Applications &amp; Interpretation. You can see what we cover in each on the <a href="classes.html">classes page</a>.</p>'),
        ("Do you teach Standard Level and Higher Level?",
         "<p>Yes. Every subject is taught at both Standard Level (SL) and Higher Level (HL). HL students also prepare for the extra components their course requires, such as Paper 3 or the HL Essay.</p>"),
        ("What is the difference between English A: Language &amp; Literature and English A: Literature?",
         "<p>Both courses study literary works and share the same assessment structure. Language &amp; Literature also studies non-literary texts, such as advertisements, speeches, articles and cartoons. Literature focuses only on literary works: poetry, prose, drama and works in translation.</p>"),
        ("What is the difference between Maths: Analysis &amp; Approaches and Applications &amp; Interpretation?",
         "<p>Analysis &amp; Approaches puts more weight on algebra, calculus and proof, and Paper 1 is taken without a calculator. Applications &amp; Interpretation puts more weight on statistics, modelling and using technology to solve problems in context.</p><p>Some university courses, particularly in mathematics, engineering and the physical sciences, ask for Analysis &amp; Approaches at HL. Check the entry requirements of the courses you are interested in before you choose.</p>"),
        ("My school is teaching a new syllabus. Do your classes follow it?",
         "<p>Yes. We teach the course that your exam session follows. The IB is revising several subjects, including History, which has a new course first examined in May 2028. Tell us your exam year when you message us and we will make sure your classes match it.</p>"),
        ("Do you help with internal assessments and coursework?",
         "<p>Yes. We guide students through each subject's internally assessed work: the Individual Oral and HL Essay in English, the historical investigation, the Geography fieldwork investigation, the Business Management research project and the mathematical exploration. We help you plan, structure and improve your work. The work you submit must be your own.</p>"),
    ]),
    ("Our classes", [
        ("What are your classes like?",
         "<p>Our classes are interactive and built around discussion. You do much of the talking: you test your ideas against other students', learn to defend them, and get feedback you can act on straight away. The aim is to understand how each subject builds an argument, so you can make that argument yourself in the exam.</p>"),
        ("Who teaches the classes?",
         "<p>Classes are led by experienced tutors who know the IB Diploma courses and their assessments well.</p>"),
        ("When do classes run?",
         '<p>Each subject page lists its class slots, with the level, day, time and format. If a subject does not show any slots yet, <a href="contact.html">message us</a> and we will tell you the current timetable.</p>'),
    ]),
    ("Joining", [
        ("How do I enquire or sign up?",
         '<p>The quickest way is WhatsApp. The button on our <a href="contact.html">contact page</a> opens a message ready to send. Fill in the student&rsquo;s name, school and year, and the subjects and levels, and we will reply with the next step. You can also email us at <a href="mailto:admin@inqedu.com">admin@inqedu.com</a>.</p>'),
        ("How much are the classes?",
         '<p>Fees depend on the subject and level. <a href="contact.html">Message us</a> with the subjects you are interested in and we will send you the current fees.</p>'),
        ("Can students join in the middle of the course?",
         "<p>Message us with the student&rsquo;s year of study and subjects. We will let you know which classes have places and how we can help you catch up on what has already been covered.</p>"),
    ]),
]


def faq_html():
    groups = []
    for heading, items in FAQS:
        qs = "".join(f"""
          <details class="faq">
            <summary>{q}</summary>
            <div class="faq-answer">{a}</div>
          </details>""" for q, a in items)
        groups.append(f"""<div class="cols">
      <p class="label">{heading}</p>
      <div class="faq-list">{qs}
      </div>
    </div>""")
    return f"""<section class="band" id="faq">
  <div class="wrap">
    <div class="band-head">
      <h2>Frequently asked questions</h2>
      <p class="measure">If your question is not answered here, message us on WhatsApp.</p>
    </div>
    <div class="faq-groups">
    {"""
    """.join(groups)}
    </div>
  </div>
</section>"""


# --------------------------------------------------------------- Contact
contact = f"""<section class="page-head">
  <div class="wrap">
    <p class="label">Contact</p>
    <h1>Message us <em>on WhatsApp</em></h1>
    <p class="lede">The quickest way to reach us is WhatsApp. Tap the button and a message opens, ready to send. Add a few details and we will reply with class times and the next step.</p>
  </div>
</section>

<section class="band band--linen">
  <div class="wrap contact">
    <div class="wa-card">
      <p class="label">WhatsApp</p>
      <p class="wa-number">{WHATSAPP_DISPLAY}</p>
      <div class="actions"><a class="btn" href="{whatsapp_link()}">Chat with us on WhatsApp</a></div>
      <div class="wa-preview">
        <p class="label">Your message will start like this</p>
        <blockquote>Hi Ink &amp; Quill! I&rsquo;d like to find out more about your IB classes.<br><br>Student&rsquo;s name:<br>School and year of study:<br>Subject(s) and level (SL or HL):</blockquote>
        <p class="small">You can edit it before you send it.</p>
      </div>
    </div>
    <aside class="stack">
      <h2 style="font-size: 1.5rem;">Prefer email?</h2>
      <dl class="details">
        <div><dt>Email</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd></div>
      </dl>
    </aside>
  </div>
</section>

{faq_html()}"""

page("contact.html", "Contact Ink &amp; Quill",
     "Message Ink and Quill on WhatsApp or by email, and read answers to common questions about IB tuition.",
     contact, "contact.html")

print("Built", len(list(OUT.rglob("*.html"))), "pages into", OUT)
