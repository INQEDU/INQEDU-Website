"""Subject information for the Ink & Quill website.

Each subject gets its own page at site/classes/<slug>.html.

TO ADD CLASS SLOTS: find the subject below and add lines to its "slots" list, like this:

    "slots": [
        {"level": "HL", "day": "Saturday", "time": "10:00 am to 12:00 pm", "format": "In person", "status": "Open"},
        {"level": "SL", "day": "Wednesday", "time": "7:00 pm to 8:30 pm", "format": "Online", "status": "Full"},
    ],

"status" can be anything short, such as Open, Full, or 2 places left.
Then run:  python3 build.py
"""

# IB subject groups, shown in this order
GROUPS = [
    ("group-1", "Group 1", "Studies in language and literature"),
    ("group-3", "Group 3", "Individuals and societies"),
    ("group-5", "Group 5", "Mathematics"),
]

SUBJECTS = [
    {
        "slug": "english-language-literature",
        "group": "group-1",
        "name": "English A: Language &amp; Literature",
        "short": "Literary works alongside the texts of everyday life, from advertisements to political speeches.",
        "intro": "This course pairs literary works with non-literary texts. One week you may study a novel, the next a political speech or an advertising campaign. The skill underneath is the same: explaining how a text is constructed to affect its audience.",
        "cover": [
            "Analysing non-literary text types: advertisements, speeches, articles, cartoons and websites",
            "Reading for audience, purpose and context",
            "Commenting on visual and structural features as well as language",
            "Choosing works, extracts and a global issue for the Individual Oral",
            "Planning and writing Paper 1 and Paper 2 under timed conditions",
            "Developing a line of inquiry for the HL Essay",
        ],
        "assessment": [
            ("Paper 1", "Guided analysis of unseen non-literary texts", "One text &middot; 1 h 15 min &middot; 35%", "Two texts &middot; 2 h 15 min &middot; 35%"),
            ("Paper 2", "Comparative essay on two literary works studied", "1 h 45 min &middot; 35%", "1 h 45 min &middot; 25%"),
            ("Individual Oral", "Fifteen-minute oral on how two works present a global issue", "30%", "20%"),
            ("HL Essay", "Essay of 1,200 to 1,500 words on one work or text", "Not taken", "20%"),
        ],
        "note": "Timings and weightings follow the current English A: Language and Literature subject guide.",
        "slots": [],
    },
    {
        "slug": "english-literature",
        "group": "group-1",
        "name": "English A: Literature",
        "short": "Poetry, prose, drama and works in translation, read closely and argued about with confidence.",
        "intro": "This course is the close study of literary works across poetry, prose, drama and literature in translation. It rewards students who can read slowly, notice precisely, and build an interpretation that is their own.",
        "cover": [
            "Close reading of unseen poetry and prose",
            "Understanding form, structure and voice in each literary genre",
            "Comparing works for Paper 2 without retelling the plot",
            "Choosing extracts and a global issue for the Individual Oral",
            "Developing a line of inquiry for the HL Essay",
        ],
        "assessment": [
            ("Paper 1", "Guided analysis of unseen literary passages", "One passage &middot; 1 h 15 min &middot; 35%", "Two passages &middot; 2 h 15 min &middot; 35%"),
            ("Paper 2", "Comparative essay on two works studied", "1 h 45 min &middot; 35%", "1 h 45 min &middot; 25%"),
            ("Individual Oral", "Fifteen-minute oral on how two works present a global issue", "30%", "20%"),
            ("HL Essay", "Essay of 1,200 to 1,500 words on one work", "Not taken", "20%"),
        ],
        "note": "Timings and weightings follow the current English A: Literature subject guide.",
        "slots": [],
    },
    {
        "slug": "business-management",
        "group": "group-3",
        "name": "Business Management",
        "short": "Business concepts and tools applied to real organisations, case studies and quantitative problems.",
        "intro": "Business Management asks you to apply theory to real organisations and make reasoned decisions. We work through the five units, the business management toolkit, and the case-study and quantitative questions that the papers are built on.",
        "cover": [
            "The five units: organisation and environment, human resources, finance and accounts, marketing, and operations",
            "Using the business management toolkit",
            "Preparing for the Paper 1 pre-released statement",
            "Quantitative questions for Paper 2",
            "The HL social enterprise case in Paper 3",
            "Planning and writing the business research project (IA)",
        ],
        "assessment": [
            ("Paper 1", "Case study based on a pre-released statement", "1 h 30 min &middot; 35%", "1 h 30 min &middot; 25%"),
            ("Paper 2", "Unseen stimulus with a quantitative focus", "1 h 30 min &middot; 35%", "1 h 45 min &middot; 30%"),
            ("Paper 3", "Social enterprise case", "Not taken", "1 h 15 min &middot; 25%"),
            ("Business research project", "Internal assessment, up to 1,800 words", "30%", "20%"),
        ],
        "note": "Timings and weightings follow the current Business Management subject guide.",
        "slots": [],
    },
    {
        "slug": "economics",
        "group": "group-3",
        "name": "Economics",
        "short": "Microeconomics, macroeconomics and the global economy, applied to real data and real policy.",
        "intro": "Economics asks you to use models, diagrams and data to explain how real economies behave and to judge the policies that shape them. We build clear diagram-based analysis, confident data-response technique, and the evaluation that the top marks require.",
        "cover": [
            "The four units: introduction to economics, microeconomics, macroeconomics and the global economy",
            "Drawing and explaining diagrams accurately",
            "Writing extended responses for Paper 1",
            "Data-response technique for Paper 2",
            "HL quantitative skills and the Paper 3 policy paper",
            "Planning and writing the portfolio of three commentaries (IA)",
        ],
        "assessment": [
            ("Paper 1", "Extended response", "1 h 15 min &middot; 30%", "1 h 15 min &middot; 20%"),
            ("Paper 2", "Data response", "1 h 45 min &middot; 40%", "1 h 45 min &middot; 30%"),
            ("Paper 3", "Policy paper", "Not taken", "1 h 45 min &middot; 30%"),
            ("Portfolio", "Internal assessment: three commentaries on news articles", "30%", "20%"),
        ],
        "note": "Timings and weightings follow the current Economics subject guide, first examined in 2022.",
        "slots": [],
    },
    {
        "slug": "geography",
        "group": "group-3",
        "name": "Geography",
        "short": "Population, climate and resources, optional themes, and the fieldwork investigation.",
        "intro": "Geography combines human and physical perspectives on how the world is changing. We build the case-study knowledge, data skills and extended writing that the papers reward, and guide you through your fieldwork investigation.",
        "cover": [
            "Core themes on population, climate and resources",
            "Optional themes for Paper 1",
            "Interpreting maps, graphs and data",
            "Structuring extended responses with case studies",
            "HL extension content for Paper 3",
            "Planning and writing the fieldwork investigation (IA)",
        ],
        "assessment": [
            ("Paper 1", "Optional themes", "Taken", "Taken"),
            ("Paper 2", "Core themes", "Taken", "Taken"),
            ("Paper 3", "HL extension", "Not taken", "Taken"),
            ("Fieldwork investigation", "Internal assessment", "25%", "20%"),
        ],
        "note": "The IB is introducing a revised Geography course, so paper formats differ between exam years. Ask us for the exact timings and weightings for your exam session.",
        "slots": [],
    },
    {
        "slug": "psychology",
        "group": "group-3",
        "name": "Psychology",
        "short": "How behaviour and the mind are studied, and how to apply research to real situations.",
        "intro": "Psychology combines biological, cognitive and sociocultural perspectives on behaviour with a strong focus on research methods. We teach the revised course first examined in May 2027: applying concepts and research to unfamiliar situations, and justifying the decisions behind a study.",
        "cover": [
            "Biological, cognitive and sociocultural perspectives",
            "The course concepts, such as bias, causality, change and measurement",
            "Applying research to unfamiliar contexts for Paper 1",
            "Research methods and class practicals for Paper 2",
            "HL data analysis for Paper 3",
            "Designing and writing the research proposal (IA)",
        ],
        "assessment": [
            ("Paper 1", "Applying concepts, content and contexts", "35%", "25%"),
            ("Paper 2", "Research methods and class practicals", "35%", "Taken"),
            ("Paper 3", "HL extension: data analysis", "Not taken", "Taken"),
            ("Research proposal", "Internal assessment", "30%", "20%"),
        ],
        "note": "This is the revised Psychology course, first examined in May 2027. Ask us for the exact HL timings and weightings for your exam session.",
        "slots": [],
    },
    {
        "slug": "maths-analysis-approaches",
        "group": "group-5",
        "name": "Mathematics: Analysis &amp; Approaches",
        "short": "Algebra, functions, calculus and proof, for students who enjoy abstract reasoning.",
        "intro": "Analysis and Approaches emphasises algebraic methods, calculus and mathematical argument. We build fluency without a calculator for Paper 1, efficient use of the graphic display calculator for Paper 2, and the problem-solving needed for HL Paper 3.",
        "cover": [
            "Number and algebra, functions, geometry and trigonometry",
            "Statistics and probability",
            "Differential and integral calculus",
            "Working without a calculator for Paper 1",
            "Problem-solving for HL Paper 3",
            "Choosing a topic and writing the mathematical exploration (IA)",
        ],
        "assessment": [
            ("Paper 1", "No calculator", "1 h 30 min &middot; 40%", "2 h &middot; 30%"),
            ("Paper 2", "Graphic display calculator required", "1 h 30 min &middot; 40%", "2 h &middot; 30%"),
            ("Paper 3", "Extended problem-solving questions", "Not taken", "20%"),
            ("Mathematical exploration", "Internal assessment", "20%", "20%"),
        ],
        "note": "Weightings follow the current subject guide. A revised Mathematics course is first examined in May 2029.",
        "slots": [],
    },
    {
        "slug": "maths-applications-interpretation",
        "group": "group-5",
        "name": "Mathematics: Applications &amp; Interpretation",
        "short": "Statistics, modelling and technology-assisted problem solving in real-world contexts.",
        "intro": "Applications and Interpretation emphasises modelling, statistics and the use of technology to solve real problems. We focus on interpreting questions set in context, using the calculator well, and communicating results clearly.",
        "cover": [
            "Number and algebra, functions, geometry and trigonometry",
            "Statistics, probability and data analysis",
            "Mathematical modelling",
            "Calculus in context",
            "Using the graphic display calculator efficiently",
            "Choosing a topic and writing the mathematical exploration (IA)",
        ],
        "assessment": [
            ("Paper 1", "Short-response questions, calculator allowed", "1 h 30 min &middot; 40%", "2 h &middot; 30%"),
            ("Paper 2", "Extended-response questions, calculator allowed", "1 h 30 min &middot; 40%", "2 h &middot; 30%"),
            ("Paper 3", "Extended problem-solving questions", "Not taken", "20%"),
            ("Mathematical exploration", "Internal assessment", "20%", "20%"),
        ],
        "note": "Weightings follow the current subject guide. A revised Mathematics course is first examined in May 2029.",
        "slots": [],
    },
]
