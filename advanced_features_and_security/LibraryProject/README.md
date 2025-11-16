## Permissions and Groups

This app uses custom permissions and groups to control access to books and libraries.  

- **Models:** Permissions defined in `Book` and `Librarian` (`can_view`, `can_create`, `can_edit`, `can_delete`, etc.)  
- **Roles:** Assigned via `UserProfile` (`Admin`, `Librarian`, `Member`)  
- **Groups:** Example groups `Admins`, `Editors`, `Viewers` with assigned permissions  
- **Views:** Protected using `@permission_required` for actions and `@user_passes_test` for role-based access  
- **Testing:** Assign users to roles/groups and verify access matches permissions  
- **Management:** Groups and permissions can be managed via Django Admin
