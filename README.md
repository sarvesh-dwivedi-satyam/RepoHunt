# RepoHunt 🔍

A lightweight developer tool built with Python and Flask to discover open-source repositories, find beginner-friendly issues, and manage your contribution journey in one simple interface.

---

## 🎯 Problem Statement

Developers and students often struggle to find suitable open-source repositories and issues that match their current skill levels. Navigating through millions of GitHub projects can be overwhelming. RepoHunt solves this by bringing targeted repository discovery, beginner-issue filtering, and personal contribution tracking together into a clean, simple workflow.

---

## 👥 Target Users

* Students starting their open-source contribution journey
* Beginner to intermediate Python and Web developers
* AI/ML learners exploring open-source tools
* Developers looking for a clean way to track open issues and personal progress

---

## 🚀 Core Features (MVP)

* **Repository Discovery:** Search repositories with real-time GitHub data.
* **Beginner Issue Finder:** Filter open issues with labels like `good first issue` and `help wanted`.
* **Smart Filtering & Sorting:** Filter by programming language, stars, and last-updated metrics.
* **Local Bookmarks:** Save interesting repositories and issues directly in your browser.
* **Contribution Tracker:** Manage your progress from *Interested* to *In Progress* and *Submitted*.
* **API Caching:** Fast performance and rate-limit protection using local SQLite caching.

---

## 🔥 What Makes RepoHunt Different?

Unlike generic search engines or complex directory lists, RepoHunt focuses strictly on the **contributor experience**. Instead of just showing top repositories, it bridges the gap between discovering a project and actually making your first pull request.

---

## 🛠️ Tech Stack

* **Backend:** Python, Flask
* **Frontend:** HTML5, CSS3, Vanilla JavaScript
* **Database & Caching:** SQLite
* **External API:** GitHub REST API
* **Testing:** Pytest
