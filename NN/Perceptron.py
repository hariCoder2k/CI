# Note that this perceptron network is only for AND and OR and cannot handle XOR
class Perceptron:
    def __init__(self,w1,w2,bias,a,theta=0):
        #Intializing all set of values for the perrceptron
        self.w1 = w1
        self.w2 = w2
        self.bias = bias
        self.alpha = a
        self.theta = theta

    def activation_function(self,x, activation):
        #Activation function to handle binary and bipolar
        if activation == "binary":
            return int(x>0)
        elif activation == "bipolar":
            return 1 if x > 0 else -1 if x <= 0 else 0
        else:
            raise ValueError("Invalid activation function")

    def weighted_sum(self,x1,x2,i):
        # Helper function for fit() to calculate weighted sum
        yin = (x1[i]*self.w1 + x2[i]*self.w2)+self.bias
        return yin

    
    def fit(self,x1,x2,t):
        # Training by means of flag list
        stop,epoch = 0,0
        yin,y=0,0
        flag = [0]*len(x1)
        while 0 in flag:
            for i in range(len(x1)):
                yin = self.weighted_sum(x1,x2,i)
                y = self.activation_function(yin,"bipolar")
                if(y == t[i]):
                    flag[i] = 1
                else:
                    #update weights and bais
                    self.w1 = self.w1 + (x1[i]*t[i]*self.alpha)
                    self.w2 = self.w2 + (x2[i]*t[i]*self.alpha)
                    self.bias =  self.bias + t[i]*self.alpha
            epoch += 1
            print("Epoch: {epoch} completed".format(epoch=epoch))
            if stop not in flag:
                break
            flag = [0]*len(x1)
        print("Training Completed")

    def predict(self,input1,input2):
        # Prediction for 2 input
        return self.activation_function((input1*self.w1 + input2*self.w2)+self.bias, activation="bipolar")

    def check_weights_bias(self):
        # Return w1,w2 and bias value
        return "\nw1:{w1}\nw2:{w2}\nbias:{b}".format(w1=self.w1,w2=self.w2,b=self.bias)

#bipolar input
x1 = [-1,1,-1,1]
x2 = [-1,-1,1,1]

# the below input for AND
# t = [-1,-1,-1,1]


# the below input for OR
t = [-1,1,1,1]

net = Perceptron(0,0,0,1)
net.fit(x1,x2,t)
print()

# i value correspond to a particular column in x1,x2,t ranging from 0 to 3
print("Prediction:")
i=2
print("Predict for {input1} & {input2} is {prediction}".format(input1=x1[i],input2=x2[i],prediction=net.predict(x1[i],x2[i])))
print("Actual value: {target}".format(target=t[i]))
print()

# Printing Parameters
print("Perceptron parameters:{param}\n".format(param=net.check_weights_bias()))