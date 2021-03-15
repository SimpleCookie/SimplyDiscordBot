create database simply_discord_bot;

CREATE TABLE user (
    username varchar(36) not null primary key,
);

CREATE TABLE runk (
    username varchar(36) not null,
    created timestamp not null,
    primary key (username, created),
    foreign key (username) references user (username),
);

