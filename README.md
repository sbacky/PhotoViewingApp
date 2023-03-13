# Photo Viewing App

The purpose of this app is to provide a simple photo viewing application to store and view photos. The application allows users to upload pictures from their computer and stores them in the application database. Users will be able to upload single pictures and pictures in bulk. Users can view photos in a grid style, or one at a time. When viewing pictures as a gird, users can select a picture and view it in fullscreen.

## Setup

Django web framework used to manage backend like handling requests and serving the correct content. Node and Webpack Manager used to manage frontend packages and dependancies. npm used to install frontend resources, like JS and CSS libraries and frameworks and webpack manager is used to bundle them. NVM used to manage Node and npm versions.

Django is used because of my comfortabliity with python and the framework. Node and npm are used because of the high level of community support and most resources support it. Webpack manager is used because of its django app that takes care of all the boilerplate setup.

Alpine and Htmx are used for their inline css style implementations of JS. Unless a lot of javascript is required, Alpine and Htmx are lightweight JS libraries that provide much of the JS functionality a modern website needs. Bulma CSS framework is used because of my familiarity with it

## Releases

Latest release: Version 0.1.0

### Version 0.1.0

First release. Used to view photos in the web browser. Add photos in the admin console at /admin. Requires a superuser account to login. Photos require a name and an image to be saved but can optionally add a description and date taken. Photos can be viewed in a single column as a list or in three columns as a chart. This can be toggled by a group of two buttons above all the pictures. Pictures can be clicked on to go to a detail page for that picture. Breadcrumbs foudn at the top of the page to inform current page and provide navigation to previous page.
