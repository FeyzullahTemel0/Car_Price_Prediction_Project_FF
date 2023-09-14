perl

# Araç Fiyat Tahmin Uygulaması

Bu uygulama tarafımca öğretilen bilgiler doğrultusundan yola çıkarak kullanıcıdan aldığı bilgileri değerlendirir ve özelliklere uygun bir arac'ın ortalama fiyat tahminini kullanıcıya sunar.

## Kullanım

Uygulamayı çalıştırmak için aşağıdaki adımları izleyin:

1. Python ve PyQt5 gereksinimlerini yükleyin:

   ```bash
   PyQt5 kurulumu:

bash

pip install PyQt5

datetime, QTimer ve QTime, Python'ın dahili modülleri olduğu için ayrıca kurulum yapmanıza gerek yoktur.

scikit-learn (sklearn) kurulumu:

bash

pip install scikit-learn

webbrowser modülü de Python'ın dahili bir modülüdür, bu nedenle ayrıca kurulum yapmanıza gerek yoktur.

pandas kurulumu:

bash

    pip install pandas

Yukarıdaki komutları kullanarak bu kütüphaneleri Python ortamınıza kurabilirsiniz. İşletim sisteminize ve Python sürümünüze göre komutlar biraz farklılık gösterebilir, bu nedenle hangi işletim sistemini ve Python sürümünü kullandığınıza bağlı olarak komutları uyarlamayı unutmayın.
    bash

python main.py

Uygulama başladığında, bir sayı çizin ve "PREDICT" düğmesine tıklayarak tahmin sonucunu alın.
