from datetime import datetime

from app import db
from sqlalchemy_utils import URLType


class ShortenURL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(URLType, unique=True)
    shortcode = db.Column(db.String(50), index=True, unique=True)
    redirect_count = db.Column(db.Integer, default=0)
    start_date = db.Column(db.DateTime, default=datetime.utcnow)
    last_seen_date = db.Column(db.DateTime)

    def __repr__(self):
        return '<URL: {}>'.format(self.url)

    def to_dict(self):
        data = {
            # 'url': self.url,
            'start_date': self.start_date.isoformat(),
            'redirect_count': self.redirect_count
        }
        if self.redirect_count > 0:
            data['last_seen_date'] = self.last_seen_date.isoformat()
        return data

