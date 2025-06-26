from django.db import models

# Create your models here.
class Voter(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    dob = models.DateField()
    street_number = models.CharField(max_length=30)
    street_name = models.CharField(max_length=30)
    apartment_number = models.CharField(max_length=30)
    zip_code = models.CharField(max_length=30)
    party_affiliation = models.CharField(max_length=30)
    precinct_number = models.CharField(max_length=30)
    v20state = models.BooleanField()
    v21town = models.BooleanField()
    v21primary = models.BooleanField()
    v22general = models.BooleanField()
    v23town = models.BooleanField()
    voter_score = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}, DOB: {self.dob}, Address: {self.street_number} {self.street_name} Apt {self.apartment_number}, Zip: {self.zip_code}, Party: {self.party_affiliation}, Precinct: {self.precinct_number}, Voter Score: {self.voter_score}, Votes: 20State: {self.v20state}, 21Town: {self.v21town}, 21Primary: {self.v21primary}, 22General: {self.v22general}, 23Town: {self.v23town}"
    
    def load_data():
        Voter.objects.all().delete()
        file_path = '/Users/salmon/Desktop/django/data/newton_voters.csv'
        f = open(file_path)
        header = f.readline()
        for line in f:
            line = line.split(',')
            voter = Voter(
                first_name=line[2],
                last_name=line[1],
                dob=line[7],
                street_number=line[3],
                street_name=line[4],
                apartment_number=line[5],
                zip_code=line[6],
                party_affiliation=line[9],
                precinct_number=line[10],
                v20state=line[11].lower() == 'true',
                v21town=line[12].lower() == 'true',
                v21primary=line[13].lower() == 'true',
                v22general=line[14].lower() == 'true',
                v23town=line[15].lower() == 'true',
                voter_score=int(line[16])
            )
        print(f"Created:{voter}")
        voter.save()
    