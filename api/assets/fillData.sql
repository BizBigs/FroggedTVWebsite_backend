insert into ftv_user(nickname, email, created_at, last_modified, password) values
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
