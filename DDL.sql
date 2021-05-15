create table user
        (ID                     varchar(8),
        username                varchar(15)not null,
        email                   varchar(15)not null,
        password                varchar(20)not null,
        permissions             varchar(15),
        primary key (ID)
        );

create table team
        (ID                     varchar(8),
        user_id                 varchar(8),
        league_id               varchar(8),
        name                    varchar(16)not null,
        wins                    numeric(2,0),
        losses                  numeric(2,0),
        primary key (ID)
        foreign key (user_id) references user(ID)
                    on delete cascade,
        foreign key (league_id) references league(ID)
                    on delete cascade
        );

create table league
        (ID                     varchar(8),
        manager_id              varchar(8),
        name                    varchar(20)not null,
        roster_size             numeric(2,0)not null,
        lineup_size             numeric(1,0)not null,
        primary key (ID)
        foreign key (manager_id) references user (ID)
                on delete cascade 
        );

create table gymnast
        (ID                     varchar(8),
        firstname               varchar(15) not null,
        lastname               varchar(15) not null,
        year                    numeric(4,0) check (year > 2020 and year < 2030),
        primary key (ID)
        );

create table lineup_slot
        (team_id                varchar(8),
         event                  varchar(20) not null,
         slot                   numeric(2,2),
         gymnast_id             varchar(8),
         primary key (team_id, event, slot),
         foreign key (gymnast_id) references gymnast (ID)
                on delete cascade
        );

create table score
        (gymnast_id             varchar(8),
        date_score              date,
        event                   varchar(20) not null,
        score                   numeric(2,2),
        primary key (gymnast_id, date_score, event),
        foreign key (gymnast_id) references gymnast_id (ID)
                on delete cascade
        );
create table section
        (course_id              varchar(8),
         sec_id                 varchar(8),
         semester               varchar(6)
                check (semester in ('Fall', 'Winter', 'Spring', 'Summer')),
         year                   numeric(4,0) check (year > 1701 and year < 2100),
         building               varchar(15),
         room_number            varchar(7),
         time_slot_id           varchar(4),
         primary key (course_id, sec_id, semester, year),
         foreign key (course_id) references course (course_id)
                on delete cascade,
         foreign key (building, room_number) references classroom (building, room_number)
                on delete set null
        );

create table teaches
        (ID                     varchar(5),
         course_id              varchar(8),
         sec_id                 varchar(8),
         semester               varchar(6),
         year                   numeric(4,0),
         primary key (ID, course_id, sec_id, semester, year),
         foreign key (course_id, sec_id, semester, year) references section (course_id, sec_id, semester, year)
                on delete cascade,
         foreign key (ID) references instructor (ID)
                on delete cascade
        );