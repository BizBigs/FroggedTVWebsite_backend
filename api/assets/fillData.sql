-- Table: public.ftv_user

-- DROP TABLE IF EXISTS public.ftv_user;

CREATE TABLE IF NOT EXISTS public.ftv_user
(
    id_user integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    email character varying(50) COLLATE pg_catalog."default" NOT NULL,
    created_at timestamp with time zone NOT NULL,
    last_modified timestamp with time zone NOT NULL,
    password character varying(20) COLLATE pg_catalog."default" NOT NULL,
    nickname character varying(20) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT ftv_user_pkey PRIMARY KEY (id_user)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.ftv_user
    OWNER to admin;

-- Table: public.ftv_blog_post

-- DROP TABLE IF EXISTS public.ftv_blog_post;

CREATE TABLE IF NOT EXISTS public.ftv_blog_post
(
    id_blog_post integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    title character varying(128) COLLATE pg_catalog."default" NOT NULL,
    content text COLLATE pg_catalog."default",
    created_at timestamp with time zone,
    last_modified timestamp with time zone,
    author_id integer NOT NULL,
    CONSTRAINT ftv_blog_post_pkey PRIMARY KEY (id_blog_post),
    CONSTRAINT "FK_FTV_BLOG_POST_FTV_USER" FOREIGN KEY (author_id)
        REFERENCES public.ftv_user (id_user) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.ftv_blog_post
    OWNER to admin;


insert into ftv_user(nickname, email, created_at, last_modified, password) values
    ('Bigs', 'bigs@discord.gg', TO_TIMESTAMP('2017-03-31 9:30:20','YYYY-MM-DD HH:MI:SS'), TO_TIMESTAMP('2017-03-31 9:30:20','YYYY-MM-DD HH:MI:SS'), 'lol'),
    ('YouYou', 'youyou@discord.gg', TO_TIMESTAMP('2017-03-31 9:30:20','YYYY-MM-DD HH:MI:SS'), TO_TIMESTAMP('2017-03-31 9:30:20','YYYY-MM-DD HH:MI:SS'), 'lol'),
    ('KeepCalm', 'keepcalm@discord.gg', TO_TIMESTAMP('2017-03-31 9:30:20','YYYY-MM-DD HH:MI:SS'), TO_TIMESTAMP('2017-03-31 9:30:20','YYYY-MM-DD HH:MI:SS'), 'lol'),
    ('Drugu', 'drugu@discord.gg', TO_TIMESTAMP('2017-03-31 9:30:20','YYYY-MM-DD HH:MI:SS'), TO_TIMESTAMP('2017-03-31 9:30:20','YYYY-MM-DD HH:MI:SS'), 'lol'),
    ('Kaoru', 'kaoru@discord.gg', TO_TIMESTAMP('2017-03-31 9:30:20','YYYY-MM-DD HH:MI:SS'), TO_TIMESTAMP('2017-03-31 9:30:20','YYYY-MM-DD HH:MI:SS'), 'lol');

insert into ftv_blog_post(title, content, created_at, last_modified, author_id) values
    ('Canard', 'lorem ipsum', TO_TIMESTAMP('2017-03-31 9:30:20','YYYY-MM-DD HH:MI:SS'), TO_TIMESTAMP('2017-03-31 9:30:20','YYYY-MM-DD HH:MI:SS'), 2),
    ('Canardv2', 'lorem ipsum', TO_TIMESTAMP('2017-03-31 9:30:20','YYYY-MM-DD HH:MI:SS'), TO_TIMESTAMP('2017-03-31 9:30:20','YYYY-MM-DD HH:MI:SS'), 2),
    ('Canardv3', 'lorem ipsum', TO_TIMESTAMP('2017-03-31 9:30:20','YYYY-MM-DD HH:MI:SS'), TO_TIMESTAMP('2017-03-31 9:30:20','YYYY-MM-DD HH:MI:SS'), 2),
    ('Connard', 'lorem ipsum', TO_TIMESTAMP('2017-03-31 9:30:20','YYYY-MM-DD HH:MI:SS'), TO_TIMESTAMP('2017-03-31 9:30:20','YYYY-MM-DD HH:MI:SS'), 3),
    ('Connardv2', 'lorem ipsum', TO_TIMESTAMP('2017-03-31 9:30:20','YYYY-MM-DD HH:MI:SS'), TO_TIMESTAMP('2017-03-31 9:30:20','YYYY-MM-DD HH:MI:SS'), 3),
    ('Connardv3', 'lorem ipsum', TO_TIMESTAMP('2017-03-31 9:30:20','YYYY-MM-DD HH:MI:SS'), TO_TIMESTAMP('2017-03-31 9:30:20','YYYY-MM-DD HH:MI:SS'), 3),
    ('alcoolo', 'lorem ipsum', TO_TIMESTAMP('2017-03-31 9:30:20','YYYY-MM-DD HH:MI:SS'), TO_TIMESTAMP('2017-03-31 9:30:20','YYYY-MM-DD HH:MI:SS'), 4),
    ('tronpa', 'lorem ipsum', TO_TIMESTAMP('2017-03-31 9:30:20','YYYY-MM-DD HH:MI:SS'), TO_TIMESTAMP('2017-03-31 9:30:20','YYYY-MM-DD HH:MI:SS'), 5),
    ('tronpaV2', 'lorem ipsum', TO_TIMESTAMP('2017-03-31 9:30:20','YYYY-MM-DD HH:MI:SS'), TO_TIMESTAMP('2017-03-31 9:30:20','YYYY-MM-DD HH:MI:SS'), 5),
    ('CanardV234', 'lorem ipsum', TO_TIMESTAMP('2017-03-31 9:30:20','YYYY-MM-DD HH:MI:SS'), TO_TIMESTAMP('2017-03-31 9:30:20','YYYY-MM-DD HH:MI:SS'), 5);
