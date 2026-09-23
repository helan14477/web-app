```python
from flask import Flask, render_template_string, jsonify
from datetime import datetime
import os
import platform

application = Flask(__name__)

# ---------------------------------------------------------
# CONFIGURATION
# ---------------------------------------------------------

GITHUB_REPO_URL = "https://github.com/your-username/your-repo-name"

APPLICATION_NAME = "DATAFLOW_CORE"

# Environment variables can be configured in Elastic Beanstalk
AWS_REGION = os.environ.get("AWS_REGION", "ap-south-1")
EB_ENVIRONMENT = os.environ.get(
    "AWS_EB_ENVIRONMENT_NAME",
    "LOCAL_DEBUG"
)

# Sample ETL metrics
ETL_STATUS = "RUNNING"
RECORDS_PROCESSED = 12540
LAST_ETL_RUN = "2026-09-23 10:45:32 UTC"

# ---------------------------------------------------------
# HTML TEMPLATE
# ---------------------------------------------------------

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">

<head>

    <meta charset="UTF-8">

    <meta name="viewport"
          content="width=device-width, initial-scale=1.0">

    <title>DATAFLOW CORE | AWS</title>

    <script src="https://cdn.tailwindcss.com"></script>

    <script>

        function updateClock() {

            const now = new Date();

            document.getElementById(
                'server-time'
            ).textContent =
                now.toISOString()
                   .replace('T', ' ')
                   .substring(0, 19) + ' UTC';

        }

        setInterval(updateClock, 1000);

        window.onload = updateClock;

    </script>

    <style>

        @import url(
            'https://fonts.googleapis.com/css2?family=Share+Tech+Mono&display=swap'
        );

        body {
            font-family: 'Share Tech Mono', monospace;
        }

        .scanlines::before {

            content: "";

            position: fixed;

            top: 0;
            left: 0;

            width: 100%;
            height: 100%;

            background:
                repeating-linear-gradient(
                    to bottom,
                    transparent,
                    transparent 2px,
                    rgba(0, 0, 0, 0.15) 3px,
                    transparent 3px
                );

            pointer-events: none;

            z-index: 50;
        }

    </style>

</head>


<body
class="bg-black text-cyan-400 min-h-screen
       flex flex-col scanlines">

<!-- =====================================================
     HEADER
===================================================== -->

<header
class="relative z-20 w-full
       border-b border-cyan-900
       bg-black/80">

    <div
    class="max-w-7xl mx-auto
           px-6 py-4
           flex justify-between items-center">

        <div class="flex items-center space-x-3">

            <div class="relative h-3 w-3">

                <div
                class="absolute h-full w-full
                       bg-cyan-500 rounded-full
                       animate-ping opacity-75">
                </div>

                <div
                class="relative h-3 w-3
                       bg-cyan-300 rounded-full">
                </div>

            </div>

            <span
            class="font-bold text-sm
                   tracking-widest
                   text-cyan-300">

                SYS_ID: DATAFLOW_CORE_1

            </span>

        </div>


        <div
        class="text-xs px-4 py-2
               rounded border
               border-cyan-900
               bg-cyan-950/50">

            AWS_REGION:
            <span class="text-white">
                {{ aws_region }}
            </span>

        </div>

    </div>

</header>


<!-- =====================================================
     MAIN
===================================================== -->

<main
class="flex-grow
       flex items-center
       justify-center
       px-6 py-10
       relative z-20">


<div
class="grid grid-cols-1
       lg:grid-cols-3
       gap-6
       w-full max-w-7xl">


<!-- =====================================================
     MAIN STATUS PANEL
===================================================== -->

<div
class="lg:col-span-2
       bg-black
       border border-cyan-900
       rounded-lg
       p-8
       shadow-lg">


<div
class="flex flex-col md:flex-row
       justify-between
       md:items-center
       border-b border-cyan-900
       pb-5 mb-6">


<div>

<p class="text-xs text-cyan-700">
APPLICATION
</p>

<h1
class="text-4xl md:text-6xl
       font-black
       text-white
       tracking-tight">

DATAFLOW_

</h1>

</div>


<div
class="text-green-400
       text-3xl md:text-5xl
       font-black">

ONLINE

</div>

</div>


<p
class="text-cyan-500
       text-lg
       leading-relaxed">

/// DATA PLATFORM NODE OPERATIONAL

</p>


<p class="mt-3 text-cyan-700">

Python Flask application successfully
deployed through AWS Elastic Beanstalk.

</p>


<p class="mt-2 text-white">

ENVIRONMENT:
<span class="text-cyan-400">
{{ env_name }}
</span>

</p>


<!-- ETL STATUS -->

<div
class="mt-8
       grid grid-cols-1
       md:grid-cols-3
       gap-4">


<div
class="bg-cyan-950/40
       border border-cyan-900
       rounded
       p-5">

<p class="text-xs text-cyan-700">
ETL_PIPELINE
</p>

<p
class="text-2xl
       text-green-400
       font-bold mt-2">

{{ etl_status }}

</p>

</div>


<div
class="bg-cyan-950/40
       border border-cyan-900
       rounded
       p-5">

<p class="text-xs text-cyan-700">
RECORDS_PROCESSED
</p>

<p
class="text-2xl
       text-white
       font-bold mt-2">

{{ records_processed }}

</p>

</div>


<div
class="bg-cyan-950/40
       border border-cyan-900
       rounded
       p-5">

<p class="text-xs text-cyan-700">
LAST_ETL_RUN
</p>

<p
class="text-sm
       text-white
       font-bold mt-3">

{{ last_etl_run }}

</p>

</div>

</div>


<!-- TERMINAL -->

<div
class="mt-8
       bg-gray-950
       border border-gray-800
       rounded
       p-5
       text-xs
       space-y-2
       text-cyan-300">


<p>
&gt; INITIALIZING DATAFLOW CORE... [OK]
</p>

<p>
&gt; CONNECTING TO AWS ENVIRONMENT... [OK]
</p>

<p>
&gt; VALIDATING FLASK APPLICATION... [OK]
</p>

<p>
&gt; INITIALIZING ETL PIPELINE... [OK]
</p>

<p>
&gt; CHECKING DATA PIPELINE STATUS... [OK]
</p>

<p>
&gt; VERIFYING APPLICATION HEALTH... [OK]
</p>

<p class="text-green-400">

&gt;&gt;&gt; DATA PLATFORM READY.

</p>

</div>

</div>


<!-- =====================================================
     RIGHT PANEL
===================================================== -->

<div
class="bg-black
       border border-cyan-900
       rounded-lg
       p-6
       flex flex-col
       justify-between">


<div>


<h2
class="text-xl
       font-bold
       text-cyan-200
       border-b
       border-cyan-900
       pb-3 mb-5">

SYSTEM_STATS

</h2>


<!-- SERVER TIME -->

<div
class="bg-cyan-950/40
       border border-cyan-900
       rounded
       p-4 mb-4">

<p class="text-xs text-cyan-700">

SERVER_TIME_UTC

</p>

<p
id="server-time"
class="text-lg
       text-white
       font-bold mt-2">

{{ current_time }}

</p>

</div>


<!-- ENVIRONMENT -->

<div
class="bg-cyan-950/40
       border border-cyan-900
       rounded
       p-4 mb-4">

<p class="text-xs text-cyan-700">

EB_ENVIRONMENT

</p>

<p
class="text-lg
       text-white
       font-bold mt-2">

{{ env_name }}

</p>

</div>


<!-- PYTHON -->

<div
class="bg-cyan-950/40
       border border-cyan-900
       rounded
       p-4">

<p class="text-xs text-cyan-700">

PYTHON_RUNTIME

</p>

<p
class="text-lg
       text-white
       font-bold mt-2">

{{ python_version }}

</p>

</div>

</div>


<!-- BUTTONS -->

<div
class="space-y-3
       pt-6
       border-t
       border-cyan-900
       mt-6">


<a
href="/health"
class="block
       text-center
       px-5 py-3
       rounded
       bg-cyan-900
       hover:bg-cyan-800
       text-white
       font-bold
       text-sm">

RUN HEALTH CHECK

</a>


<a
href="/api/status"
class="block
       text-center
       px-5 py-3
       rounded
       bg-gray-900
       hover:bg-gray-800
       text-cyan-300
       border border-gray-700
       font-bold
       text-sm">

API STATUS

</a>


<a
href="{{ github_url }}"
target="_blank"
class="block
       text-center
       px-5 py-3
       rounded
       bg-gray-900
       hover:bg-gray-800
       text-cyan-300
       border border-gray-700
       font-bold
       text-sm">

SOURCE CODE

</a>

</div>

</div>

</div>

</main>


<!-- =====================================================
     FOOTER
===================================================== -->

<footer
class="relative z-20
       border-t border-cyan-950
       py-4
       text-center
       text-xs
       text-cyan-800">

[DATAFLOW_CORE_RUNNING]
>>
AWS ELASTIC BEANSTALK
>>
PYTHON / FLASK
>>
ETL READY

</footer>


</body>
</html>
"""


# =========================================================
# ROUTES
# =========================================================

@application.route("/")
def home():

    now = datetime.utcnow().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    return render_template_string(

        HTML_TEMPLATE,

        current_time=now,

        github_url=GITHUB_REPO_URL,

        env_name=EB_ENVIRONMENT,

        aws_region=AWS_REGION,

        etl_status=ETL_STATUS,

        records_processed=f"{RECORDS_PROCESSED:,}",

        last_etl_run=LAST_ETL_RUN,

        python_version=platform.python_version()
    )


# =========================================================
# HEALTH CHECK
# =========================================================

@application.route("/health")
def health_check():

    return jsonify({

        "status": "healthy",

        "application":
            APPLICATION_NAME,

        "service":
            "flask",

        "environment":
            EB_ENVIRONMENT,

        "aws_region":
            AWS_REGION,

        "timestamp_utc":
            datetime.utcnow().isoformat(),

        "python_version":
            platform.python_version()

    }), 200


# =========================================================
# API STATUS
# =========================================================

@application.route("/api/status")
def api_status():

    return jsonify({

        "application":
            APPLICATION_NAME,

        "deployment":
            "AWS Elastic Beanstalk",

        "status":
            "RUNNING",

        "etl_pipeline":
            ETL_STATUS,

        "records_processed":
            RECORDS_PROCESSED,

        "last_etl_run":
            LAST_ETL_RUN,

        "environment":
            EB_ENVIRONMENT,

        "region":
            AWS_REGION

    }), 200


# =========================================================
# LOCAL DEVELOPMENT
# =========================================================

if __name__ == "__main__":

    application.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )
```

### `requirements.txt`

```text
Flask==3.1.2
gunicorn==23.0.0
```

### `.ebextensions/python.config`

```yaml
option_settings:
  aws:elasticbeanstalk:container:python:
    WSGIPath: application:application
```

### Project structure

```text
dataflow-core/
│
├── application.py
│
├── requirements.txt
│
└── .ebextensions/
    │
    └── python.config
```

### Deploy to Elastic Beanstalk

From the project directory:

```bash
eb init
```

Select your AWS region, then Python platform.

Create the environment:

```bash
eb create dataflow-core-env
```

Deploy:

```bash
eb d
```
