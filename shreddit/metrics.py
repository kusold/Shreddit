from prometheus_client import CollectorRegistry, Counter, Gauge, Summary, push_to_gateway


registry = CollectorRegistry()
COMMENT_DELETED_COUNT = Counter('reddit_comments_deleted', 'Count of comments removed', registry=registry)
COMMENT_WHITELISTED_COUNT = Counter('reddit_comments_whitelisted', 'Count of comments whitelisted', registry=registry)
COMMENT_RECENT_COUNT = Counter('reddit_comment_recent', 'Count of comments whitelisted', registry=registry)
SUBMISSION_DELETED_COUNT = Counter('reddit_submissions_deleted', 'Count of comments removed', registry=registry)
JOB_TIME = Summary('job_processing_seconds', 'Time spent by job', registry=registry)
JOB_LAST_SUCCESS = Gauge('job_last_success_unixtime', 'Last time a batch job successfully finished', registry=registry)

def push_metrics(uri, job, username):
  push_to_gateway(uri, job=job, registry=registry, grouping_key={'username': username})
