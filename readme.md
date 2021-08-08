# Blog-app API by Django REST API

### Description
___

this is a personal blog project which user (owner website) can share projects and articles for
a reader also creat, update or delete a post (projects, article).

following app-relations

![Application relation](/resource/blog-app-relations.png)

___

### Application have to

1. API for **User/Profile** which...

    - [x] can login to get a token for autherize for do other actions.
    - [x] update user profile.
    - [x] after **add User** (on admin page) user **Profile** have to auto generate and prefill some data.
    - [x] after **delete** profile, user must auto delete.

2. API for **Project** which...

    - [x] can create a project.
    - [x] can update a project.
    - [x] can delete a project.
    - [x] can get all a projects.
    - [x] can get a project by id.
    - [x] can search projects by title or tag.

3. API for **Article** which...

    - [ ] can create a article.
    - [ ] can update a article.
    - [ ] can delete a article.
    - [ ] can get all an articles.
    - [ ] can get an article by id.
    - [x] can search articles by title or description.

4. API for **Tag** which...

    - [x] can create a tag and **must check** if a tag is existing should not create new one.
    - [ ] can delete a tag.
