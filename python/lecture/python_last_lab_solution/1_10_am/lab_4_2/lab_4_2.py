import numpy as np


def make_cards(array):
    ######################################
    # TODO :  get_winner 함수를 구현하시오.  
    #         [Input]
    #         - array : (N,) 1-d array  
    #  
    #         [output]
    #         - cards :  (number of people=5, 5) reshaped of array 
    # ========== EDIT HERE ==========
	np.random.shuffle(array)
    cards = array.reshape(5,5)
    # ===============================
    return cards

def get_winner(cards): 
    ######################################
    # TODO :  get_winner 함수를 구현하시오.  
    #         [Input]
    #         - cards : (number of people=5, 5)  
    #  
    #         [output]
    #         - winner :  합이 가장 큰 사람 (index가 0인 사람이 첫번째 사람)
    # ========== EDIT HERE ==========
    I = np.eye(5)
    diagonal_matrix = np.multiply(cards,I)
    U = np.ones((5,5))
    I_minus_U = I - U
    negative_diagonal_matrix = np.multiply(cards,I_minus_U)
    combined_matrix = np.add(diagonal_matrix, negative_diagonal_matrix)
    sum_matrix = combined_matrix.sum(axis=1)
    winner = np.argmax(sum_matrix) + 1
    # ===============================
    return winner

if __name__ == '__main__':
    # ========== EDIT HERE ==========
    # TODO : make random array (25,1)
    array = np.arange(1,26)
    # ===============================
    cards = make_cards(array)
    winner = get_winner(cards)

    print(winner)


