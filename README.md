# pyGitlabIssueBoard
写个能便捷提交issue的python小工具

## 思路
我们一个人需要对应多个项目，此时用不同的程序提交issue很麻烦，就用一个程序通过不同项目的access token来对应多个项目的issue。
access token存储在sqlite3的db内。

## resource
1. gitlab_rest_api_document [https://docs.gitlab.cn/jh/api/rest/]
2. 