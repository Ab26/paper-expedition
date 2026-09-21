CREATE TABLE `reading` (
	`id` text PRIMARY KEY NOT NULL,
	`status` text DEFAULT 'Not started' NOT NULL,
	`notes` text DEFAULT '{}' NOT NULL,
	`confidence` integer DEFAULT 0 NOT NULL,
	`updated` text NOT NULL
);
--> statement-breakpoint
CREATE TABLE `settings` (
	`id` text PRIMARY KEY NOT NULL,
	`start` text NOT NULL
);
