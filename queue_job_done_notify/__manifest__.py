{
    "name": "Queue Job Web Done Notify",
    "summary": """
        This module allows to display a notification to the related user of a
        done job. It uses the web_notify notification feature.""",
    "version": "14.0.1.0.0",
    "author": "Muhammad Rizqi",
    "website": "https://github.com/muhrizky",
    "license": "AGPL-3",
    "category": "Generic Modules",
    "depends": [
        # OCA/queue
        "queue_job",
        # OCA/web
        "web_notify",
    ],
    "data": ["views/queue_job_function.xml"],
}
