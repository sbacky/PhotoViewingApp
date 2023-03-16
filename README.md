# Photo Viewing App

The purpose of this projec is to provide a simple photo viewing application to store and view photos in the web browser (That isnt social media). The application allows users to upload pictures from their computer and store them in the application database. Users will be able to upload pictures one at a time. Users can view photos in a grid style, or as a list. Wether viewing pictures as a gird or a list, users can select a picture and view it in fullscreen from a detail page.

Latest Release: [Version 0.1.1](#version-011)

## Setup

Django web framework used to manage backend like handling requests and serving the correct content. Node and Webpack Manager used to manage frontend packages and dependancies. npm used to install frontend resources, like JS and CSS libraries and frameworks and webpack manager is used to bundle them. NVM used to manage Node and npm versions.

Django is used because of my comfortabliity with python and the framework. Node and npm are used because of the high level of community support and most resources support it. Webpack manager is used because of its django app that takes care of all the boilerplate setup.

Alpine and Htmx are used for their inline css style implementations of JS. Unless a lot of javascript is required, Alpine and Htmx are lightweight JS libraries that provide much of the JS functionality a modern website needs. Bulma CSS framework is used because of my familiarity with it

## Releases

Latest release: Version 0.1.1

### Version 0.1.0

First release. Used to view photos in the web browser. Add photos in the admin console at /admin. Requires a superuser account to login. Photos require a name and an image to be saved but can optionally add a description and date taken.

Photos can be viewed in a list view or a column view. List view: 1 photo takes up the available space and you have to scroll down to view the next photo. Column view displays 3 photos in a row for as many rows that fit in the available space and you have to scroll down to view more rows. This can be toggled by a group of two buttons above all the pictures. When in list view, photos turn slightly opaque when hovered. When in column view, pictures get slightly zoomed in when hovered.

Pictures can be clicked on to go to a detail page for that picture. Detail pages are found at /photo_id. Detail pages display the same information as on the home page but the image takes up all the available space and you can only view one image at a time. Breadcrumbs found at the top of the page to inform current page and provide navigation to previous page.

### Version 0.1.1

Fixed issue with load pictures button. Button style would not consistently match column style. Made button sonsistently full width regardless of list or column display.

Added secondary button to take user to top. Button grouped with load more pictures button and is primary. When no more pictures to load (no next page) load pictures button is hidden and this button takes up the additional space, spanning across all three columns.

### Future Releases

Add categories to photos as a way to organize and sort/filter them. Can add categores as a foriegn key relationship or as a parameter on photos. Create a menu in sidebar to navigate different categories.

Add Logo to nav bar and on home page.

Add a previous and next button on the detail page. Previous button takes you to previous image relative to home view. Next button takes you to the next image relative to the home view.

Add user account creation and login support to secure application by making users sign in to accounts to access app. Users will not be able to create an account on there own but will require a system administrator (Superuser) to create an account for them. User class to keep track of user defining information. Profile class for how the user interacts with the application.
