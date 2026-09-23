# ```python
# from flask import Flask, render_template_string, jsonify
# from datetime import datetime
# import os
# import platform

# # ============================================================
# # APPLICATION CONFIGURATION
# # ============================================================

# GITHUB_REPO_URL = "https://github.com/your-username/your-repo-name"

# application = Flask(__name__)

# APPLICATION_NAME = "DATAHUB_CORE"

# # Read AWS / Elastic Beanstalk environment variables
# AWS_REGION = os.environ.get("AWS_REGION", "ap-south-1")
# ENV_NAME = os.environ.get(
#     "AWS_EB_ENVIRONMENT_NAME",
#     "LOCAL_DEVELOPMENT"
# )

# # Sample application metrics
# RECORDS_PROCESSED = 12540
# ETL_STATUS = "ACTIVE"
# DATA_SOURCE = "AMAZON S3"
# TARGET_SYSTEM = "AWS GLUE"
# LAST_RUN = "2026-09-23 10:45:32 UTC"


# # ============================================================
# # HTML TEMPLATE
# # ============================================================

# HTML_TEMPLATE = """
# <!DOCTYPE html>

# <html lang="en">

# <head>

#     <meta charset="UTF-8">

#     <meta name="viewport"
#           content="width=device-width, initial-scale=1.0">

#     <title>
#         DATAHUB CORE | AWS Elastic Beanstalk
#     </title>

#     <script src="https://cdn.tailwindcss.com"></script>

#     <script>

#         function updateClock() {

#             const now = new Date();

#             document.getElementById(
#                 'server-time'
#             ).textContent =
#                 now.toISOString()
#                    .replace('T', ' ')
#                    .substring(0, 19)
#                    + ' UTC';
#         }

#         setInterval(updateClock, 1000);

#         window.onload = updateClock;

#     </script>


#     <style>

#         @import url(
#             'https://fonts.googleapis.com/css2?family=Share+Tech+Mono&display=swap'
#         );


#         body {

#             font-family:
#                 'Share Tech Mono',
#                 monospace;

#         }


#         .scanlines::before {

#             content: "";

#             position: fixed;

#             top: 0;
#             left: 0;

#             width: 100%;
#             height: 100%;

#             background:
#                 repeating-linear-gradient(
#                     to bottom,
#                     transparent,
#                     transparent 2px,
#                     rgba(0, 0, 0, 0.15) 3px,
#                     transparent 3px
#                 );

#             pointer-events: none;

#             z-index: 50;

#         }


#         .glow {

#             text-shadow:
#                 0 0 5px #22d3ee,
#                 0 0 10px #22d3ee;

#         }


#     </style>

# </head>


# <body
#     class="
#         bg-black
#         text-cyan-400
#         min-h-screen
#         flex
#         flex-col
#         scanlines
#     ">


# <!-- ==========================================================
#      HEADER
# =========================================================== -->

# <header
#     class="
#         relative
#         z-20
#         w-full
#         border-b
#         border-cyan-900
#         bg-black/80
#     ">

#     <div
#         class="
#             max-w-7xl
#             mx-auto
#             px-6
#             py-4
#             flex
#             justify-between
#             items-center
#         ">


#         <!-- SYSTEM ID -->

#         <div
#             class="
#                 flex
#                 items-center
#                 space-x-3
#             ">

#             <div
#                 class="
#                     relative
#                     h-3
#                     w-3
#                 ">

#                 <div
#                     class="
#                         absolute
#                         h-full
#                         w-full
#                         bg-cyan-500
#                         rounded-full
#                         animate-ping
#                         opacity-75
#                     ">
#                 </div>

#                 <div
#                     class="
#                         relative
#                         h-3
#                         w-3
#                         bg-cyan-300
#                         rounded-full
#                     ">
#                 </div>

#             </div>


#             <span
#                 class="
#                     font-bold
#                     text-sm
#                     tracking-widest
#                     text-cyan-300
#                 ">

#                 SYS_ID: DATAHUB_CORE_1

#             </span>

#         </div>


#         <!-- AWS REGION -->

#         <div
#             class="
#                 text-xs
#                 px-4
#                 py-2
#                 rounded
#                 border
#                 border-cyan-900
#                 bg-cyan-950/50
#             ">

#             AWS_REGION:

#             <span class="text-white">

#                 {{ aws_region }}

#             </span>

#         </div>

#     </div>

# </header>


# <!-- ==========================================================
#      MAIN
# =========================================================== -->

# <main
#     class="
#         flex-grow
#         flex
#         items-center
#         justify-center
#         px-6
#         py-10
#         relative
#         z-20
#     ">


# <div
#     class="
#         grid
#         grid-cols-1
#         lg:grid-cols-3
#         gap-6
#         w-full
#         max-w-7xl
#     ">


# <!-- ==========================================================
#      LEFT PANEL
# =========================================================== -->

# <div
#     class="
#         lg:col-span-2
#         bg-black
#         border
#         border-cyan-900
#         p-8
#         rounded-lg
#         shadow-inner
#     ">


#     <!-- TITLE -->

#     <div
#         class="
#             flex
#             flex-col
#             md:flex-row
#             md:items-center
#             md:justify-between
#             border-b
#             border-cyan-900
#             pb-5
#             mb-6
#         ">


#         <div>

#             <p
#                 class="
#                     text-xs
#                     text-cyan-700
#                     tracking-widest
#                 ">

#                 DATA PLATFORM

#             </p>


#             <h1
#                 class="
#                     text-4xl
#                     md:text-6xl
#                     font-black
#                     text-white
#                     tracking-tight
#                 ">

#                 DATAHUB_

#             </h1>

#         </div>


#         <span
#             class="
#                 text-3xl
#                 md:text-5xl
#                 font-black
#                 text-green-400
#                 mt-4
#                 md:mt-0
#             ">

#             ONLINE

#         </span>

#     </div>


#     <!-- STATUS -->

#     <div
#         class="
#             text-cyan-600
#             text-lg
#             leading-relaxed
#         ">


#         <p class="animate-pulse">

#             /// STATUS:
#             DATA PROCESSING NODE OPERATIONAL.

#         </p>


#         <p class="mt-2">

#             AWS Elastic Beanstalk successfully
#             initialized with Python / Flask runtime.

#         </p>


#         <p class="mt-2 text-white">

#             ENVIRONMENT:

#             <span class="text-cyan-400">

#                 {{ env_name }}

#             </span>

#         </p>

#     </div>


#     <!-- ======================================================
#          DATA PIPELINE
#     ======================================================= -->

#     <div
#         class="
#             mt-8
#             grid
#             grid-cols-1
#             md:grid-cols-3
#             gap-4
#         ">


#         <!-- SOURCE -->

#         <div
#             class="
#                 bg-cyan-950/40
#                 border
#                 border-cyan-900
#                 rounded
#                 p-5
#             ">

#             <p
#                 class="
#                     text-xs
#                     text-cyan-700
#                 ">

#                 DATA_SOURCE

#             </p>


#             <p
#                 class="
#                     text-xl
#                     text-white
#                     font-bold
#                     mt-2
#                 ">

#                 {{ data_source }}

#             </p>

#         </div>


#         <!-- ETL -->

#         <div
#             class="
#                 bg-cyan-950/40
#                 border
#                 border-cyan-900
#                 rounded
#                 p-5
#             ">

#             <p
#                 class="
#                     text-xs
#                     text-cyan-700
#                 ">

#                 PIPELINE_STATUS

#             </p>


#             <p
#                 class="
#                     text-xl
#                     text-green-400
#                     font-bold
#                     mt-2
#                 ">

#                 {{ etl_status }}

#             </p>

#         </div>


#         <!-- TARGET -->

#         <div
#             class="
#                 bg-cyan-950/40
#                 border
#                 border-cyan-900
#                 rounded
#                 p-5
#             ">

#             <p
#                 class="
#                     text-xs
#                     text-cyan-700
#                 ">

#                 TARGET_SYSTEM

#             </p>


#             <p
#                 class="
#                     text-xl
#                     text-white
#                     font-bold
#                     mt-2
#                 ">

#                 {{ target_system }}

#             </p>

#         </div>

#     </div>


#     <!-- ======================================================
#          RECORD METRICS
#     ======================================================= -->

#     <div
#         class="
#             mt-4
#             bg-cyan-950/20
#             border
#             border-cyan-900
#             rounded
#             p-5
#         ">


#         <div
#             class="
#                 flex
#                 justify-between
#                 items-center
#             ">


#             <div>

#                 <p
#                     class="
#                         text-xs
#                         text-cyan-700
#                     ">

#                     RECORDS_PROCESSED

#                 </p>


#                 <p
#                     class="
#                         text-3xl
#                         text-white
#                         font-bold
#                         mt-2
#                     ">

#                     {{ records_processed }}

#                 </p>

#             </div>


#             <div>

#                 <p
#                     class="
#                         text-xs
#                         text-cyan-700
#                         text-right
#                     ">

#                     LAST_PIPELINE_RUN

#                 </p>


#                 <p
#                     class="
#                         text-sm
#                         text-cyan-300
#                         mt-2
#                     ">

#                     {{ last_run }}

#                 </p>

#             </div>

#         </div>

#     </div>


#     <!-- ======================================================
#          TERMINAL
#     ======================================================= -->

#     <div
#         class="
#             mt-8
#             bg-gray-950
#             border
#             border-gray-800
#             rounded
#             p-5
#             text-xs
#             space-y-2
#             text-cyan-300
#         ">


#         <p>

#             &gt; INITIALIZING DATAHUB CORE... [OK]

#         </p>


#         <p>

#             &gt; CONNECTING TO AMAZON S3... [OK]

#         </p>


#         <p>

#             &gt; VALIDATING DATA SOURCE... [OK]

#         </p>


#         <p>

#             &gt; INITIALIZING ETL PIPELINE... [OK]

#         </p>


#         <p>

#             &gt; CHECKING AWS ENVIRONMENT... [OK]

#         </p>


#         <p>

#             &gt; STARTING FLASK APPLICATION... [OK]

#         </p>


#         <p class="text-green-400">

#             &gt;&gt;&gt; DATA PLATFORM READY.

#         </p>

#     </div>

# </div>


# <!-- ==========================================================
#      RIGHT PANEL
# =========================================================== -->

# <div
#     class="
#         bg-black
#         border
#         border-cyan-900
#         p-6
#         rounded-lg
#         shadow-inner
#         flex
#         flex-col
#         justify-between
#     ">


# <div>


#     <h2
#         class="
#             text-xl
#             font-bold
#             text-cyan-200
#             uppercase
#             border-b
#             border-cyan-900
#             pb-3
#             mb-5
#         ">

#         SYSTEM_STATS

#     </h2>


#     <!-- SERVER TIME -->

#     <div
#         class="
#             bg-cyan-950/40
#             p-4
#             rounded
#             border
#             border-cyan-900
#             mb-4
#         ">

#         <p
#             class="
#                 text-xs
#                 text-cyan-600
#             ">

#             SERVER_TIME_UTC

#         </p>


#         <p
#             id="server-time"
#             class="
#                 text-lg
#                 text-white
#                 font-bold
#                 mt-2
#             ">

#             {{ current_time }}

#         </p>

#     </div>


#     <!-- ENVIRONMENT HEALTH -->

#     <div
#         class="
#             bg-cyan-950/40
#             p-4
#             rounded
#             border
#             border-cyan-900
#             mb-4
#         ">

#         <p
#             class="
#                 text-xs
#                 text-cyan-600
#             ">

#             ENVIRONMENT_HEALTH

#         </p>


#         <p
#             class="
#                 text-green-400
#                 font-bold
#                 mt-2
#                 text-lg
#                 flex
#                 items-center
#                 space-x-2
#             ">


#             <span
#                 class="
#                     relative
#                     flex
#                     h-3
#                     w-3
#                 ">

#                 <span
#                     class="
#                         animate-ping
#                         absolute
#                         inline-flex
#                         h-full
#                         w-full
#                         rounded-full
#                         bg-green-400
#                         opacity-75
#                     ">
#                 </span>


#                 <span
#                     class="
#                         relative
#                         inline-flex
#                         rounded-full
#                         h-3
#                         w-3
#                         bg-green-500
#                     ">
#                 </span>

#             </span>


#             <span>

#                 NOMINAL

#             </span>

#         </p>

#     </div>


#     <!-- PYTHON VERSION -->

#     <div
#         class="
#             bg-cyan-950/40
#             p-4
#             rounded
#             border
#             border-cyan-900
#         ">

#         <p
#             class="
#                 text-xs
#                 text-cyan-600
#             ">

#             PYTHON_RUNTIME

#         </p>


#         <p
#             class="
#                 text-lg
#                 text-white
#                 font-bold
#                 mt-2
#             ">

#             {{ python_version }}

#         </p>

#     </div>

# </div>


# <!-- ======================================================
#      ACTION BUTTONS
# ======================================================= -->

# <div
#     class="
#         space-y-3
#         pt-6
#         border-t
#         border-cyan-900
#         mt-6
#     ">


#     <a
#         href="/health"
#         class="
#             block
#             w-full
#             text-center
#             px-6
#             py-3
#             rounded
#             bg-cyan-900
#             hover:bg-cyan-800
#             text-white
#             font-bold
#             text-sm
#             uppercase
#             tracking-wider
#         ">

#         RUN HEALTH CHECK

#     </a>


#     <a
#         href="/api/status"
#         class="
#             block
#             w-full
#             text-center
#             px-6
#             py-3
#             rounded
#             bg-gray-900
#             hover:bg-gray-800
#             text-cyan-300
#             font-bold
#             text-sm
#             border
#             border-gray-700
#         ">

#         VIEW API STATUS

#     </a>


#     <a
#         href="{{ github_url }}"
#         target="_blank"
#         class="
#             block
#             w-full
#             text-center
#             px-6
#             py-3
#             rounded
#             bg-gray-900
#             hover:bg-gray-800
#             text-cyan-300
#             font-bold
#             text-sm
#             border
#             border-gray-700
#         ">

#         SOURCE CODE

#     </a>

# </div>


# </div>


# </div>

# </main>


# <!-- ==========================================================
#      FOOTER
# =========================================================== -->

# <footer
#     class="
#         relative
#         z-20
#         py-4
#         text-center
#         text-xs
#         text-cyan-900
#         border-t
#         border-cyan-950
#         w-full
#         bg-black/50
#     ">

#     [DATAHUB_CORE_RUNNING]
#     >>
#     AWS ELASTIC BEANSTALK
#     >>
#     FLASK
#     >>
#     ETL READY

# </footer>


# </body>

# </html>
# """


# # ============================================================
# # HOME PAGE
# # ============================================================

# @application.route("/")
# def home():

#     now = datetime.utcnow().strftime(
#         "%Y-%m-%d %H:%M:%S"
#     )

#     return render_template_string(

#         HTML_TEMPLATE,

#         current_time=now,

#         github_url=GITHUB_REPO_URL,

#         env_name=ENV_NAME,

#         aws_region=AWS_REGION,

#         data_source=DATA_SOURCE,

#         target_system=TARGET_SYSTEM,

#         etl_status=ETL_STATUS,

#         records_processed=f"{RECORDS_PROCESSED:,}",

#         last_run=LAST_RUN,

#         python_version=platform.python_version()

#     )


# # ============================================================
# # HEALTH CHECK
# # ============================================================

# @application.route("/health")
# def health_check():

#     return jsonify({

#         "status": "healthy",

#         "application":
#             APPLICATION_NAME,

#         "service":
#             "Flask",

#         "environment":
#             ENV_NAME,

#         "aws_region":
#             AWS_REGION,

#         "etl_status":
#             ETL_STATUS,

#         "timestamp_utc":
#             datetime.utcnow().isoformat(),

#         "python_version":
#             platform.python_version()

#     }), 200


# # ============================================================
# # API STATUS
# # ============================================================

# @application.route("/api/status")
# def api_status():

#     return jsonify({

#         "application":
#             APPLICATION_NAME,

#         "deployment":
#             "AWS Elastic Beanstalk",

#         "status":
#             "RUNNING",

#         "data_source":
#             DATA_SOURCE,

#         "target_system":
#             TARGET_SYSTEM,

#         "etl_pipeline":
#             ETL_STATUS,

#         "records_processed":
#             RECORDS_PROCESSED,

#         "last_etl_run":
#             LAST_RUN,

#         "environment":
#             ENV_NAME,

#         "aws_region":
#             AWS_REGION

#     }), 200


# # ============================================================
# # LOCAL DEVELOPMENT
# # ============================================================

# if __name__ == "__main__":

#     application.run(

#         host="0.0.0.0",

#         port=5000,

#         debug=False

#     )
# ```
