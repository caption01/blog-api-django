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

    - [ ] can login to get a token for autherize for do other actions.
    - [ ] update user profile.
    - [ ] after **add User** (on admin page) user **Profile** have to auto generate and prefill some data.
    - [ ] after **delete** profile, user must auto delete.

2. API for **Project** which...

    - [ ] can create a project.
    - [ ] can update a project.
    - [ ] can delete a project.
    - [ ] can get all a projects.
    - [ ] can get a project by id.
    - [ ] can filter projects by title or tag.

3. API for **Article** which...

    - [ ] can create a article.
    - [ ] can update a article.
    - [ ] can delete a article.
    - [ ] can get all an articles.
    - [ ] can get an article by id.
    - [ ] can filter articles by title or description.

4. API for **Tag** which...

    - [ ] can create a tag and **must check** if a tag is existing should not create new one.
    - [ ] can delete a tag.
