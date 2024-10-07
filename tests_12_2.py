import unittest

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.run1 = Runner('Усэйн', 10)
        self.run2 = Runner('Андрей', 9)
        self.run3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results:
            formatted_result = '{' + ', '.join(f'{place}: {runner}' for place, runner in result.items()) + '}'
            print(formatted_result)

    def test_tournament_usain_nick(self):
        tournament = Tournament(90, self.run1,self.run3)
        results1 = tournament.start()
        self.all_results.append(results1)
        self.assertTrue(results1[max(results1.keys())] == 'Ник')


    def test_tournament_andrey_nick(self):
        tournament = Tournament(90, self.run2, self.run3)
        results2 = tournament.start()
        self.all_results.append(results2)
        self.assertTrue(results2[max(results2.keys())] == 'Ник')



    def test_tournament_usain_andrey_nick(self):
        tournament = Tournament(90, self.run1, self.run2, self.run3)
        results3 = tournament.start()
        self.all_results.append(results3)
        self.assertTrue(results3[max(results3.keys())] == 'Ник')

if __name__ == "__main__":
    unittest.main()


