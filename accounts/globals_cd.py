POSITION_CD = (
    ('P01', 'Physician - General Medicine'),
    ('P02', 'Physician - Critical Care'),
    ('P03', 'Physician - Emergency'),
    ('N01', 'Nurse'),
    ('N02', 'Nurse - ICU'),
    ('N03', 'Nurse - Emergency'),
    ('N04', 'Nurse - Ambulatory'),
    ('CEO', 'Chief Executive Officer'),
    ('CFO', 'Chief Financial Officer'),
    ('COO', 'Chief Operating Officer'),
    ('M01', 'General Manager'),
)

MEDIA_CHOICES = (
    ('Audio', (
            ('vinyl', 'Vinyl'),
            ('cd', 'CD'),
        )
    ),
    ('Video', (
            ('vhs', 'VHS Tape'),
            ('dvd', 'DVD'),
        )
    ),
    ('unknown', 'Unknown'),
)
