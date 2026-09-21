import { sqliteTable, text, integer } from 'drizzle-orm/sqlite-core';
export const reading = sqliteTable('reading', {id:text('id').primaryKey(), status:text('status').notNull().default('Not started'),notes:text('notes').notNull().default('{}'),confidence:integer('confidence').notNull().default(0),updated:text('updated').notNull()});
export const settings = sqliteTable('settings',{id:text('id').primaryKey(),start:text('start').notNull()});
