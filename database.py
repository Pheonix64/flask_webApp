from sqlalchemy import create_engine, text

engine = create_engine("mysql+pymysql://root@localhost/goyetchetchiyan?charset=utf8mb4")


def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs"))
    
    jobs = []
    for row in result.all():
        jobs.append(row._asdict())
    return jobs    
