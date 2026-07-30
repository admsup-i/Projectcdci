from flask import Flask, render_template, jsonify
import datetime

app = Flask(__name__)

APP_VERSION = "1.0.0"

PROFILE = {
    "name": "Iliyas Ahemad Siddiqui",
    "title": "Site Reliability Engineer | Production Support & Cloud Reliability",
    "location": "Hyderabad, India",
    "email": "siddiqui.i1988@gmail.com",
    "phone": "+91 8125957278",
    "linkedin": "https://linkedin.com/in/iliyas-siddiqui-4a8b20ab",
    "summary": (
        "Site Reliability & Production Support engineer with 13+ years driving uptime, "
        "incident response, and release reliability for enterprise and cloud SaaS platforms. "
        "Experienced leading a 9-engineer support POD against SLO/error-budget targets, with "
        "hands-on depth in Kubernetes/Docker, CI/CD pipelines, Python automation, and "
        "observability (Splunk, Dynatrace, Prometheus, Grafana)."
    ),
    "skills": [
        {"category": "Leadership & Management", "skill_list": ["Team Lead (9 engineers)", "Mentoring", "On-call Planning", "Incident Command", "Process Improvement"]},
        {"category": "Reliability & Observability", "skill_list": ["SLI/SLO Design", "Error Budgets", "Splunk", "Dynatrace", "Prometheus", "Grafana"]},
        {"category": "Containers & CI/CD", "skill_list": ["Kubernetes", "Docker", "GitHub Actions", "Release Automation"]},
        {"category": "Automation & IaC", "skill_list": ["Python", "Shell Scripting", "Terraform"]},
        {"category": "Service Management", "skill_list": ["ITIL", "RCA & Postmortems", "Change Management"]},
        {"category": "Cloud Platforms", "skill_list": ["AWS (EC2, S3, VPC, ASG)", "Azure (VM, Storage, DB)"]},
        {"category": "Languages & Databases", "skill_list": ["Java", "SQL", "MySQL", "MariaDB"]},
        {"category": "Tools", "skill_list": ["ServiceNow", "Jira", "Confluence", "LaunchDarkly", "F5"]},
    ],
    "experience": [
        {
            "role": "Senior Cloud Support Engineer (SSE1) – POD Lead",
            "company": "Atlassian",
            "location": "Hyderabad",
            "period": "Mar 2022 – Present",
            "highlights": [
                "POD lead for 9 support engineers — workload, mentoring, SLO/error-budget tracking, SLA adherence",
                "Led critical incident and mass-outage response; drove blameless post-incident reviews",
                "Directed monitoring strategy across Splunk, Dynatrace, Prometheus, and Grafana",
                "Introduced AI capabilities into support tooling and CI/CD pipeline improvements",
            ],
        },
        {
            "role": "Senior Reliability Engineer",
            "company": "ServiceNow",
            "location": "Hyderabad",
            "period": "Feb 2019 – Mar 2022",
            "highlights": [
                "Owned application performance, stability, and availability against SLO/error-budget targets",
                "Automated recurring operational checks with Python/Ansible, reducing manual toil",
                "Advanced troubleshooting via heap/thread dumps and log analysis",
            ],
        },
        {
            "role": "Senior Software Engineer (Application & Technical Support)",
            "company": "Trianz Holdings",
            "location": "",
            "period": "Jan 2018 – Feb 2019",
            "highlights": [
                "End-to-end technical/application support and production incident triage within SLA",
                "Managed release operations, coordinating deployment validation with engineering",
            ],
        },
        {
            "role": "Senior Process Associate (Developer & Support)",
            "company": "Tata Consultancy Services",
            "location": "",
            "period": "Feb 2016 – Jan 2018",
            "highlights": [
                "Application/technical support for Java-based enterprise systems",
                "Automated repetitive support processes, reducing manual effort",
            ],
        },
        {
            "role": "Analyst",
            "company": "Serco (Google India Project)",
            "location": "",
            "period": "Oct 2013 – Jul 2015",
            "highlights": [
                "Technical/operational support for large-scale Google Maps data systems",
                "Managed database operations and stored procedures for production data pipelines",
            ],
        },
        {
            "role": "Support Engineer",
            "company": "Incline Technologies",
            "location": "",
            "period": "Mar 2012 – Jun 2013",
            "highlights": [
                "L1/L2 technical and application support, incident handling, server monitoring",
            ],
        },
    ],
    "education": [
        {"degree": "MCM – Master in Computer Management", "school": "Pune University", "period": "2009–2011"},
        {"degree": "BCA – Bachelor of Computer Applications", "school": "SRTM University", "period": "2006–2009"},
    ],
    "achievements": [
        "Led a 9-member support POD against SLO/error-budget targets, ensuring consistent SLA achievement",
        "Reduced recurring incidents through structured RCA, blameless postmortems, and preventive action",
        "Introduced Python/Ansible automation and CI/CD improvements that cut manual operational toil",
        "Streamlined troubleshooting processes and knowledge base content, cutting resolution time and ramp-up",
    ],
}


@app.route("/")
def home():
    return render_template("index.html", profile=PROFILE, version=APP_VERSION)


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat()
    }), 200


@app.route("/api/profile")
def api_profile():
    return jsonify(PROFILE)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
