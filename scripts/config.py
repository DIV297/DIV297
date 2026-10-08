"""Everything personal lives here. Edit this file, re-run `python scripts/render_all.py`."""

USERNAME = "DIV297"
NAME = "Divansh Bajaj"
PROMPT_USER = "divansh"
PROMPT_HOST = "github"

# Cycled by the typing animation in header.svg
ROLES = [
    "Lead Engineer @ chitragupta-bharat",
    "AWS Certified Developer",
    "Full-Stack, Cloud & Serverless Architect",
    "Building AI Agents with Vertex AI + Google ADK",
]

TAGLINE = "Bengaluru, IN  ·  shipping cloud-native products & AI agents"

# neofetch-style rows on info-card.svg. "{...}" placeholders are filled from live data.
INFO_ROWS = [
    ("Role", "Lead Engineer @ chitragupta-bharat"),
    ("Location", "Bengaluru, Karnataka"),
    ("Cert", "AWS Certified Developer – Associate"),
    ("Uptime", "{uptime} on GitHub"),
    ("Langs", "{top_langs}"),
    ("Frontend", "React · Next.js · TypeScript"),
    ("Backend", "Node.js · Express · Python · MongoDB"),
    ("Cloud", "AWS Lambda · API Gateway · DynamoDB · GCP"),
    ("AI", "Vertex AI · Google ADK · LLM Agents"),
    ("Repos", "{public_repos} public  ·  {stars} stars"),
    ("Activity", "{total} contributions this year"),
    ("Streak", "{current_streak}d current  ·  {longest_streak}d best"),
]

# globe.svg: home pin + arcs to the cloud regions you ship to (lat, lon)
HOME = ("Bengaluru", 12.97, 77.59)
REGIONS = [
    ("ap-south-1", 19.08, 72.88),
    ("ap-southeast-1", 1.35, 103.82),
    ("eu-central-1", 50.11, 8.68),
    ("us-east-1", 38.95, -77.45),
    ("asia-northeast1", 35.68, 139.69),
]

# tech-sphere.svg: category -> labels (each category gets its own colour)
TECH = {
    "frontend": ["React", "Next.js", "TypeScript", "JavaScript", "Tailwind"],
    "backend": ["Node.js", "Express", "Python", "MongoDB", "REST", "Stripe"],
    "cloud": ["AWS Lambda", "API Gateway", "DynamoDB", "S3", "Serverless", "GCP"],
    "ai": ["Vertex AI", "Google ADK", "AI Agents", "LLMs"],
    "tools": ["Docker", "Git", "GitHub Actions"],
}
