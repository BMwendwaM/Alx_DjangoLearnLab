** Django Blog Authentication System **

1. Overview

This project adds a complete user authentication system to the django_blog application.
It enables users to:
-- Register an account
-- Log in
-- Log out
-- Manage and update their profile (username, email, bio, profile picture)
The goal is to improve personalization and give users control over their information.

2. Features Implemented

-- User Registration
Users can create an account using a registration form that includes username, email, and password.
Validation ensures password strength and checks for duplicate users.
After registration, users are redirected to the login page.
-- User Login & Logout
Django's built-in authentication system manages login and logout securely.
Users are redirected appropriately after logging in or out.
Unauthorized users cannot access profile pages.
-- Profile Management
The system allows users to update:
Username
Email
Bio
Profile Picture

The profile page is only accessible to authenticated users.
Updated data is validated, saved, and confirmed with user feedback messages.
Automatic Profile Creation
A Profile model extends the default Django User model with extra fields.
Profile creation is automated using Django signals, so every user always has a linked profile.

3. Templates

Custom templates were created for:
Registration
Login
Profile Page
Base layout (for shared styling)

All templates include:
Form error display
CSRF protection
Links for navigation between auth pages

4. URL Configuration

Dedicated routes handle all authentication:
/register/
/login/
/logout/
/profile/
This keeps the authentication system organized and accessible.

5. Security

The system implements several security measures:
CSRF tokens for every form
Secure password hashing (Django default)
Access control for profile pages (login required)
Field validation during registration and updates

6. Testing Summary

To verify functionality:
Registration
Create a user
Confirm user appears in the database
Confirm profile auto-creates

Login/Logout
Ensure login works with correct credentials
Ensure logout redirects properly

Profile Update
Change username, email, bio, picture
Confirm data saves and updates


** BLOG POST FEATURES **

The blog post management system in this Django project allows users to create, view, update and delete posts seamlessly.
Authenticated users can create new posts and edit or delete only the posts they authored, while all users can view post 
lists and details.
Each CRUD operation is backed by Django class-based views, forms and templates, with proper access control enforced using 
LoginRequiredMixin and UserPassesTestMixin.
Templates provide user-friendly interfaces for listing posts, viewing full content, submitting forms and confirming 
deletions.
The system has been thoroughly tested to ensure secure data handling, correct form validation, and smooth navigation 
between views.


** COMMENT SYSTEM FEATURE **
Users can view comments under each blog post.
Authenticated users can add, edit, or delete their own comments.
Permissions ensure only the author of a comment can modify or remove it.
The system validates comment content and prevents empty submissions.
URLs for comment operations are intuitive:

posts/<post_id>/comments/new/ → Add a comment
comments/<comment_id>/edit/ → Edit a comment
comments/<comment_id>/delete/ → Delete a comment

Templates are integrated into the blog post detail page for seamless user interaction.
Testing ensures correct functionality and secure access control.


** Tags Feature **
Posts now support tagging using django-taggit.
Tags can be added during post creation or editing as comma-separated values.
Tags are displayed on each post and clicking a tag shows all posts using that tag.
A search bar allows searching posts by title, content, or tag name.
Search results are shown on a dedicated results page.