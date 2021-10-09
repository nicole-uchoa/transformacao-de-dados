import tabula 
import zipfile 


def quadro30():
    df = tabula.read_pdf("padrao_tiss_componente_organizacional_202108.pdf", pages = "108")
    quadro30 = df[0]
    quadro30[['Código', 'Descrição da categoria']] = quadro30["Tabela de Tipo do Demandante"].str.split(n=1, expand=True)
    quadro30= quadro30.drop(columns=['Tabela de Tipo do Demandante'])
    quadro30 = quadro30.drop(0)
    quadro30.to_csv('tabela_de_tipo_do_demandante.csv', index=False)

def quadro31():
    df = tabula.read_pdf("padrao_tiss_componente_organizacional_202108.pdf", pages = "109,110,111,112,113,114")
    quadro31_1 = df[0]
    quadro31_2 = df[1]
    quadro31_3 = df[2]
    quadro31_4 = df[3]
    quadro31_5 = df[4]
    quadro31_6 = df[5]
    quadro31_1 = quadro31_1.rename(columns={'Unnamed: 0':'Código', 'Tabela de Categoria do Padrão TISS':'Descrição da categoria'})
    quadro31_1 = quadro31_1.drop(0)
    quadro31_1.to_csv('tabela_de_categoria_padrao_tiss.csv', index=False,)
    quadro31_2.to_csv('tabela_de_categoria_padrao_tiss.csv', mode='a', index=False,)
    quadro31_3.to_csv('tabela_de_categoria_padrao_tiss.csv', mode='a', index=False,)
    quadro31_4.to_csv('tabela_de_categoria_padrao_tiss.csv', mode='a', index=False,)
    quadro31_5.to_csv('tabela_de_categoria_padrao_tiss.csv', mode='a', index=False,)
    quadro31_6.to_csv('tabela_de_categoria_padrao_tiss.csv', mode='a', index=False,)

def quadro32():
    df = tabula.read_pdf("padrao_tiss_componente_organizacional_202108.pdf", pages = "114")
    quadro32 = df[1]
    quadro32[['Código', 'Descrição de categoria']] = quadro32["Tabela de Tipo de Solicitação"].str.split(n=1, expand=True)
    quadro32 = quadro32.drop(columns=['Tabela de Tipo de Solicitação'])
    quadro32 = quadro32.drop([0,1,4])
    quadro32.to_csv('tabela_de_tipo_de_solicitação.csv', index=False)

quadro30()
quadro31()
quadro32()

z = zipfile.ZipFile('Teste_Intuituve_Care.zip', 'w', zipfile.ZIP_DEFLATED)
z.write('tabela_de_tipo_do_demandante.csv')
z.write('tabela_de_tipo_do_demandante.csv')
z.write('tabela_de_categoria_padrao_tiss.csv')
z.close()