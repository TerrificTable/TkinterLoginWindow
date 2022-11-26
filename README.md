# TkinterLoginWindow
Login window and registering with mysql and tkinter


It uses [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) for the ui<

For username and password storing it uses mysql (you can use `freesqldatabase.com` if you want to test using a free database) it DOES NOT encrypt any data stored, you can impleemnt that yourself if you want to

You can create the database table using this sql code: ```sql
CREATE TABLE `test` (
	`id` INT(11) NOT NULL AUTO_INCREMENT,
	`username` TEXT NOT NULL COLLATE 'latin1_swedish_ci',
	`password` TEXT NOT NULL COLLATE 'latin1_swedish_ci',
	`signup` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY (`id`) USING BTREE
)
COLLATE='latin1_swedish_ci'
ENGINE=InnoDB
AUTO_INCREMENT=0;
```
