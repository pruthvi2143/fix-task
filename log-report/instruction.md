# Access-log summary report

The file `/app/access.log` holds Apache/Nginx "combined"-style access log lines,
one request per line, for example:

    192.168.0.1 - - [16/Jun/2026:10:00:01 +0000] "GET /index.html HTTP/1.1" 200 1024

Analyze the traffic and write a JSON summary to `/app/report.json`.

## Output

`/app/report.json` must be a single JSON object with exactly these three keys:

- `total_requests` (integer): the number of request lines in the log — count
  every non-empty line.
- `unique_ips` (integer): the number of distinct client IP addresses, where the
  client IP is the first whitespace-separated field on each line.
- `top_path` (string): the request path requested most often. The path is the
  second token inside the quoted request (e.g. `/index.html` in
  `"GET /index.html HTTP/1.1"`). If two paths tie on count, choose the one that
  sorts first alphabetically.

Example shape (illustrative values, not the answer):

    {"total_requests": 10, "unique_ips": 4, "top_path": "/index.html"}

## Success criteria

1. `/app/report.json` exists and parses as a single JSON object.
2. `total_requests` equals the number of request lines in `/app/access.log`.
3. `unique_ips` equals the number of distinct client IP addresses in the log.
4. `top_path` is the most-requested path (alphabetically first on a tie).

You have 120 seconds to complete this task.
