-- drop database if exists simply_discord_bot;
-- create database simply_discord_bot;
-- use simply_discord_bot;

CREATE TABLE IF NOT EXISTS member (
    username varchar(36) not null primary key
);

CREATE TABLE IF NOT EXISTS runk (
    username varchar(36) not null,
    created timestamp not null,
    foreign key (username) references member (username)
);

CREATE TABLE IF NOT EXISTS command (
    phrase varchar(36) not null primary key,
    msg varchar(256) not null
);
