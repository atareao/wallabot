
<!-- start project-info -->
<!--
project_title: wallabot
github_project: https://github.com/atareao/wallabot
license: MIT
icon: /datos/Sync/Programacion/docker/wallabot/wallabot.svg
homepage: https://www.atareao.es/aplicacion/wallabot
license-badge: True
contributors-badge: True
lastcommit-badge: True
codefactor-badge: True
--->

<!-- end project-info -->

<!-- start badges -->

![License MIT](https://img.shields.io/badge/license-MIT-green)
![Contributors](https://img.shields.io/github/contributors-anon/atareao/wallabot)
![Last commit](https://img.shields.io/github/last-commit/atareao/wallabot)
[![CodeFactor](https://www.codefactor.io/repository/github/atareao/wallabot/badge/master)](https://www.codefactor.io/repository/github/atareao/wallabot/overview/master)
<!-- end badges -->

<!-- start description -->
<h1 align="center">Welcome to <span id="project_title">wallabot</span> 👋</h1>
<p>
<a href="https://www.atareao.es/aplicacion/wallabot" id="homepage" rel="nofollow">
<img align="right" height="128" id="icon" src="wallabot.svg" width="128"/>
</a>
</p>
<h2>🏠 <a href="https://www.atareao.es/aplicacion/wallabot" id="homepage">Homepage</a></h2>
<p>Readme Maker is a simple application to help you to make your README files</p>

<!-- end description -->

<!-- start prerequisites -->
## Prerequisites

All prerequisites are in the Docker File

<!-- end prerequisites -->

<!-- start installing -->
## Installing <span id="project_title">wallabot</span>

To install <span id="project_title">wallabot</span>, follow these steps:

### Docker

```
docker run -d --name=wallabot \
-p 5000:5000 \
-v database:/app/database \
--env-file ./.env
atareao/wallabot:amd64
```

Also you can use the `docker-compose.yml`. This is for using with Traefik, but must be work without it anyway.


<!-- end installing -->

<!-- start using -->
## Using <span id="project_title">wallabot</span>

Before you start the wallabot app, you must get a Telegram Bot working. So you  have the required parameter.


The webhook is a the endpoint, you must tell Telegram to point to. If your url is `https://wallabot.tuservidor.com`, and the WEBHOOK is `bfc7dabd-27ef-4f27-9eeb-55726e388335`... You must tell Telegram following url `https://wallabot.tuservidor.com/webhook/bfc7dabd-27ef-4f27-9eeb-55726e388335` (remember add `/webhook/` path to url before uuid).

To get a webhook you can use a [uuid generator](https://www.uuidgenerator.net/)

### Wallabag

In order to get this bot working, you must configure a Wallabag client. In the `.env` file, you must configure following parameters,

* `CLIENT_ID` the `id` of your wallabag client
* `CLIENT_SECRET` the `secret` of your wallabag client
* `USERNAME` the `username` of your wallabag user
* `PASSWORD` the `password` of your wallabag user
* `WALLABAG_BASE_URI` the `uri` of your wallabag instance

<!-- end using -->

<!-- start contributing -->
## Contributing to <span id="project_title">wallabot</span>

To contribute to **<span id="project_title">wallabot</span>**, follow these steps:

1. Fork this repository.
2. Create a branch: `git checkout -b <branch_name>`.
3. Make your changes and commit them: `git commit -m '<commit_message>'`
4. Push to the original branch: `git push origin atareao/readmemaker`
5. Create the pull request.

Alternatively see the GitHub documentation on [creating a pull request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).
</commit_message></branch_name>

<!-- end contributing -->

<!-- start contributors -->
## 👤 Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):




<!-- end contributors -->

<!-- start table-contributors -->

<table id="contributors">
	<tr id="info_avatar">
		<td id="atareao" align="center">
			<a href="https://github.com/atareao">
				<img src="https://avatars3.githubusercontent.com/u/298055?v=4" width="100px"/>
			</a>
		</td>
	</tr>
	<tr id="info_name">
		<td id="atareao" align="center">
			<a href="https://github.com/atareao">
				<strong>Lorenzo</strong>
			</a>
		</td>
	</tr>
	<tr id="info_commit">
		<td id="atareao" align="center">
			<a href="/commits?author=atareao">
				<span id="role">💻</span>
			</a>
		</td>
	</tr>
</table>
<!-- end table-contributors -->
