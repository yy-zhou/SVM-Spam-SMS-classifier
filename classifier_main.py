__author__ = 'BorisMirage'
# --- coding:utf-8 ---

'''
Create by BorisMirage
File Name: classifier_main
Create Time: 2018-12-02 16:23
'''

import classifier_bayes
import classifier_svm
import numpy as np
import read_data_file


def bayes(training, training_label, test_set, test_label_set, vocabulary_list):
    c = classifier_bayes.NaiveBayesClassifier(training, training_label, test_set, test_label_set, vocabulary_list)
    bayes_out = c.performance()
    return bayes_out


def svm(training, training_label, test_set, test_label_set, vocabulary_list):
    c = classifier_svm.SVMClassifier(training, training_label, test_set, test_label_set, vocabulary_list)
    svm_out = c.performance()
    return svm_out


def stat_all(bayes_out, svm_out, r):
    print("")
    print("Naive Bayes Classifier Statistics for %d rounds:" % r)
    print("Average time: %.2fs" % np.mean(bayes_out[0]))
    print("Average recall rate: %.2f%%" % np.mean(bayes_out[1]))
    print("Average precision rate: %.2f%%" % np.mean(bayes_out[2]))
    print("Average error rate: %.2f%%" % np.mean(bayes_out[3]))

    print("")
    print("SVM Classifier Statistics for %d rounds:" % r)
    print("Average time: %.2fs" % np.mean(svm_out[0]))
    print("Average recall rate: %.2f%%" % np.mean(svm_out[1]))
    print("Average precision rate: %.2f%%" % np.mean(svm_out[2]))
    print("Average error rate: %.2f%%" % np.mean(svm_out[3]))


def single_test(msg, train_size, test_size):
    c = classifier_bayes.NaiveBayesClassifier(train_size, test_size)
    c.single_input_classification(msg)
    c1 = classifier_svm.SVMClassifier(train_size, test_size)
    c1.single_input_classification(msg)


def get_data_set(training_size, test_size):
    return read_data_file.read(training_size, test_size)


def result(tss, ts_size, tr):
    # Type check
    if type(tr) is not int:
        raise TypeError("Wrong type! 'round' parameter should be integer!")
    if tr < 1:
        raise ValueError("Round # should larger than 1!")

    bayes_time, bayes_recall, bayes_precision, bayes_err = np.zeros(tr), np.zeros(tr), np.zeros(tr), np.zeros(tr)

    svm_time, svm_recall, svm_precision, svm_err = np.zeros(tr), np.zeros(tr), np.zeros(tr), np.zeros(tr)

    b = []
    s = []
    for i in range(0, tr):
        training, training_label, test_set, test_label_set, vocabulary_list = get_data_set(tss, ts_size)

        print("Bayes Round %d:" % i + 1)
        br = bayes(training, training_label, test_set, test_label_set, vocabulary_list)
        bayes_time[i], bayes_recall[i], bayes_precision[i], bayes_err[i] = br[0], br[1], br[2], br[3]

        print("SVM Round %d:" % i + 1)
        sr = svm(training, training_label, test_set, test_label_set, vocabulary_list)
        svm_time[i], svm_recall[i], svm_precision[i], svm_err[i] = sr[0], sr[1], sr[2], sr[3]

    b.append(bayes_time)
    b.append(bayes_recall)
    b.append(bayes_precision)
    b.append(bayes_err)

    s.append(svm_time)
    s.append(svm_recall)
    s.append(svm_precision)
    s.append(svm_err)
    stat_all(b, s, tr)


if __name__ == '__main__':
    """
    Unit test
    """

    training_set_size = 800
    test_set_size = 300
    test_round = 20
    result(training_set_size, test_set_size, test_round)
    # d = get_data_set(training_set_size, test_set_size)
    # b = bayes(d[0], d[1], d[2], d[3], d[4], test_round)
    # s = svm(d[0], d[1], d[2], d[3], d[4], test_round)
    # statistics(b, s)
    # msg = "Our biggest sale of the year is coming to a close, don't miss your chance to save up to 50% on your favorites including Epionce, SkinMedica, Jurlique, and many more!"
    # single_test(msg, 400, 1)
