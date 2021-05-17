create table users
        (ID                     varchar(8),
        username                varchar(50)not null,
        email                   varchar(50)not null,
        password                varchar(50)not null,
        primary key (ID)
        );

create table league
        (ID                     varchar(8),
        manager_id              varchar(8),
        name                    varchar(300)not null,
        roster_size             numeric(2,0)not null,
        lineup_size             numeric(1,0)not null,
        primary key (ID),
        foreign key (manager_id) references users (ID)
                on delete cascade 
        );

create table team
        (ID                     varchar(8),
        user_id                 varchar(8),
        league_id               varchar(8),
        name                    varchar(300)not null,
        wins                    numeric(2,0),
        losses                  numeric(2,0),
        primary key (ID),
        foreign key (user_id) references users(ID)
                    on delete cascade,
        foreign key (league_id) references league(ID)
                    on delete cascade
        );

create table gymnast
        (ID                     varchar(8),
        name               		varchar(50) not null,
        year                    numeric(4,0) check (year >= 2000 and year <= 2030),
        primary key (ID)
        );

create table lineup_slot
        (team_id                varchar(8),
         event                  varchar(20) not null,
         slot                   numeric(2,0),
         gymnast_id             varchar(8),
         primary key (team_id, event, slot),
         foreign key (team_id) references team (ID)
                on delete cascade,
         foreign key (gymnast_id) references gymnast (ID)
                on delete cascade
        );

create table score
        (gymnast_id             varchar(8),
        date_score              date,
        event                   varchar(20) not null,
        score                   numeric(2,0),
        score_id 		varchar(8),
        primary key (gymnast_id, date_score, event, score_id),
        foreign key (gymnast_id) references gymnast (ID)
                on delete cascade
        );
create table user_league
        (user_id                varchar(8),
         league_id              varchar(8),
         primary key (user_id, league_id),
         foreign key (user_id) references users (ID)
                on delete cascade,
         foreign key (league_id) references league (ID)
                on delete cascade
        );

create table roster
        (team_id                varchar(8),
         gymnast_id             varchar(8),
         primary key (team_id, gymnast_id),
         foreign key (team_id) references team (ID)
                on delete cascade,
         foreign key (gymnast_id) references gymnast (ID)
                on delete cascade
        );

create table matchup
        (team_id                varchar(8),
        opponent_id             varchar(8),
        week                    varchar(10),
        primary key(team_id, opponent_id, week),
        foreign key(team_id) references team (ID)
                on delete cascade,
        foreign key(opponent_id) references team (ID)
                on delete cascade
        );