create table submissions (
	id serial primary key,
	submission_title text not null,
	submission_id text not null,
	submission_score numeric(10,2),
	submission_url text not null,
	submission_author text not null
	);
