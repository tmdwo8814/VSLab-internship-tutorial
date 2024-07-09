import torch
import torch.nn as nn

import torchvision.datasets as dsets
import torchvision.transforms as tranforms

import torch.nn.init

# device 설정
device = 'cuda' if torch.cuda.is_available() else 'cpu'

torch.manual_seed(777)
if device == 'cuda':
    torch.cuda.manual_seed_all(777)

# set parameter
learning_rate = 1e-3
epochs = 15
batch_size = 100

# load dataset
mnist_train = dsets.MNIST(root='MNIST_data/',
                            train=True,
                            transform=tranforms.ToTensor(),
                            download=True)

mnist_test = dsets.MNIST(root='MNIST_data/',
                            train=False,
                            transform=tranforms.ToTensor(),
                            download=True)

# set dataloader
data_loader = torch.utils.data.DataLoader(dataset=mnist_train,
                                        batch_size=batch_size,
                                        shuffle=True,
                                        drop_last=True)

# modeling
class CNN(nn.Module):
    def __init__(self):
        super(CNN, self).__init__()
        self.layer1 = nn.Sequential(
            nn.Conv2d(1, 32, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2)
        )

        self.layer2 = nn.Sequential(
            nn.Conv2d(32, 64, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2)
        )

        self.fc = nn.Linear(7*7*64, 10, bias=True)
        torch.nn.init.xavier_uniform_(self.fc.weight)

    def forward(self, x):
        out = self.layer1(x)
        out = self.layer2(out)

        out = out.view(out.size(0), -1)
        out = self.fc(out)
        return out

# set to training
print(device)

model = CNN().to(device)

criterion = nn.CrossEntropyLoss().to(device)
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

# training
total_batch = len(data_loader)

print('start!!!!!!!!')

for epoch in range(epochs):
    avg_cost = 0

    for x, y in data_loader:
        x = x.to(device)
        y = y.to(device)

        optimizer.zero_grad()
        hypothesis = model(x)

        cost = criterion(hypothesis, y)
        cost.backward()
        optimizer.step()

        avg_cost += cost / total_batch
    
    print('[Epoch : {}] cost = {}'.format(epoch+1, avg_cost))

print('finish!!!!!')  


# inference
with torch.no_grad():
    X_test = mnist_test.test_data.view(len(mnist_test), 1, 28, 28).float().to(device)
    Y_test = mnist_test.test_labels.to(device)

    prediction = model(X_test)

    correct_prediction = torch.argmax(prediction, 1) == Y_test
    accuracy = correct_prediction.float().mean()
    print('accuracy : {}'.format(accuracy.item()))

