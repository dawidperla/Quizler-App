from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:


    def __init__(self, quiz_brain: QuizBrain ):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizler")
        self.window.config(padx = 20, pady = 20, bg = THEME_COLOR)


        self.score = Label(text = f"Score: 0 ", fg = "white", bg = THEME_COLOR)
        self.score.grid(row = 0, column = 1)


        self.canvas = Canvas(height = 250, width = 300, bg = "white")
        self.question_text = self.canvas.create_text(150,125,width = 280, text = "Some Question bla bla", fill = THEME_COLOR, font = ("Arial", 20, "italic"))
        self.canvas.grid(row = 1, column = 0, columnspan = 2, pady = 50)


        self.ok_image = PhotoImage(file = "images/true.png")
        self.nok_image = PhotoImage(file = "images/false.png")
        self.button_ok = Button(image = self.ok_image, command = self.true_button)
        self.button_nok = Button(image = self.nok_image, command = self.false_button)
        self.button_ok.grid(row = 2, column = 0)
        self.button_nok.grid(row = 2, column = 1)
        self.get_next_question()


        self.window.mainloop()
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text = f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text = q_text)
        else:
            self.canvas.itemconfig(self.question_text, text = "Właśnie wyczerpałeś wszystkie pytania i zakończyłeś QUIZ")
            self.button_nok.config(state = "disabled")
            self.button_ok.config(state="disabled")


    def true_button(self):
        self.give_feedback(self.quiz.check_answer("True"))


    def false_button(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)


    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

# e = QuizInterface
# e()