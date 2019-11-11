from django.test import TestCase
from quizer_game.models import Quiz, Question, Choice, Player


class PlayerModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        quiz = Quiz.objects.create(topic='Python Programming')
        question = Question.objects.create(quiz=quiz, text='What is str?', number=1)
        Player.objects.create(quiz=quiz, current_question=question,
                              name='Player1', selected_difficulty=0)

    def setUp(self) -> None:
        quiz = Quiz.objects.create(topic='Python Programming')
        question = Question.objects.create(quiz=quiz, text='What is str?', number=1)
        self.player = Player.objects.create(quiz=quiz, current_question=question,
                                            name='Player2', selected_difficulty=0)

    def test_quiz_label(self):
        """Test verbose name of quiz (ForeignKey)"""
        player = Player.objects.get(id=1)
        field_label = player._meta.get_field('quiz').verbose_name
        self.assertEquals(field_label, 'Quiz')

    def test_current_question_label(self):
        """Test verbose name of current question (ForeignKey)"""
        player = Player.objects.get(id=1)
        field_label = player._meta.get_field('current_question').verbose_name
        self.assertEquals(field_label, 'current question')

    def test_name_label(self):
        """Test verbose name of name (CharField)"""
        player = Player.objects.get(id=1)
        field_label = player._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'Name')

    def test_time_label(self):
        """Test verbose name of time (TimeField)"""
        player = Player.objects.get(id=1)
        field_label = player._meta.get_field('time').verbose_name
        self.assertEquals(field_label, 'Time spent')

    def test_selected_difficulty_label(self):
        """Test verbose name of selected difficulty (IntegerField)"""
        player = Player.objects.get(id=1)
        field_label = player._meta.get_field('selected_difficulty').verbose_name
        self.assertEquals(field_label, 'Difficulty')

    def test_position_label(self):
        """Test verbose name of position (IntegerField)"""
        player = Player.objects.get(id=1)
        field_label = player._meta.get_field('position').verbose_name
        self.assertEquals(field_label, 'position')

    def test_is_playing_label(self):
        """Test verbose name of is playing (BooleanField)"""
        player = Player.objects.get(id=1)
        field_label = player._meta.get_field('is_playing').verbose_name
        self.assertEquals(field_label, 'is playing')

    def test_is_failed_label(self):
        """Test verbose name of is failed (BooleanField)"""
        player = Player.objects.get(id=1)
        field_label = player._meta.get_field('is_failed').verbose_name
        self.assertEquals(field_label, 'Fail status')

    def test_is_achieved_label(self):
        """Test verbose name of is achieved (BooleanField)"""
        player = Player.objects.get(id=1)
        field_label = player._meta.get_field('is_achieved').verbose_name
        self.assertEquals(field_label, 'Achieve status')

    def test_name_max_length(self):
        """Test max length of name (CharField)"""
        player = Player.objects.get(id=1)
        field_max_length = player._meta.get_field('name').max_length
        self.assertEquals(field_max_length, 200)

    def test_selected_difficulty_default(self):
        """Test default value of selected difficulty (IntegerField)"""
        player = Player.objects.get(id=1)
        field_default = player._meta.get_field('selected_difficulty').default
        self.assertEquals(field_default, 0)

    def test_position_default(self):
        """Test default value of position (IntegerField)"""
        player = Player.objects.get(id=1)
        field_default = player._meta.get_field('position').default
        self.assertEquals(field_default, 0)

    def test_is_playing_default(self):
        """Test default value of is playing (BooleanField)"""
        player = Player.objects.get(id=1)
        field_default = player._meta.get_field('is_playing').default
        self.assertFalse(field_default)

    def test_is_failed_default(self):
        """Test default value of is failed (BooleanField)"""
        player = Player.objects.get(id=1)
        field_default = player._meta.get_field('is_failed').default
        self.assertFalse(field_default)

    def test_is_achieved_default(self):
        """Test default value of is achieved (BooleanField)"""
        player = Player.objects.get(id=1)
        field_default = player._meta.get_field('is_achieved').default
        self.assertFalse(field_default)

    def test_move_forward(self):
        """move_forward() move Player position +1 unit without saving"""
        old_position = self.player.position
        self.player.move_forward()
        self.player.save()
        self.assertEquals(self.player.position, old_position + 1)

    def test_move_backward(self):
        """move_forward() move Player position -1 unit without saving"""
        old_position = self.player.position
        self.player.move_backward()
        self.player.save()
        self.assertEquals(self.player.position, old_position - 1)
