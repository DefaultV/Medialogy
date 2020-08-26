using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class AtomScript : MonoBehaviour {

    private int Protons;
    private int Neutrons;
    private int Electrons;
    private List<Transform> RingList;

    public GameObject g_proton;
    public GameObject g_neutron;
    public GameObject g_electron;
    public GameObject Radioactive;

    private Transform cloud_core;

    public Text AtomInfoText;



    void Start () {
		

        cloud_core = GetChildWithName("Core");
	}
	
	void Update () {
        KeyBoardDebug();
        RotateCore();
	}

    void KeyBoardDebug()
    {
        string input = Input.inputString;
        switch (input)
        {
            case "p":
                AddProton();
                break;
            case "n":
                AddNeutron();
                break;
            case "e":
                AddElectron();
                break;

            case "P":
                RemoveProton();
                break;
            case "N":
                RemoveNeutron();
                break;
            case "E":
                RemoveElectron();
                break;

			

        }
    }

    AtomScript()
    {
        this.Protons = 0;
        this.Neutrons = 0;
        this.Electrons = 0;
    }

    public void Purge()
    {
        for (int i = 0; i < GetChildWithName("Outer Ring").childCount; i++)
        {
            Destroy(GetChildWithName("Outer Ring").GetChild(i).gameObject);
        }
        for (int i = 0; i < GetChildWithName("Inner Ring").childCount; i++)
        {
            Destroy(GetChildWithName("Inner Ring").GetChild(i).gameObject);
        }
        for (int i = 0; i < GetChildWithName("Core").childCount; i++)
        {
            Destroy(GetChildWithName("Core").GetChild(i).gameObject);
        }
        this.Protons = 0;
        this.Neutrons = 0;
        this.Electrons = 0;
        UpdateStructure();
    }

    public void RemoveProton()
    {
        foreach (Transform child in cloud_core)
        {
					if (child.name == "Proton(Clone)")
            {
                Destroy(child.gameObject);
                this.Protons--;
                break;
            }
        }
        UpdateStructure();
    }
	public GameObject cannon_PS;
	void ShootCannon(){
		cannon_PS.GetComponent<ParticleSystem> ().Emit (1);
	}

    public void RemoveNeutron()
    {
        foreach (Transform child in cloud_core)
        {
            if (child.name == "Neutron(Clone)")
            {
                Destroy(child.gameObject);
                this.Neutrons--;
                break;
            }
        }
        UpdateStructure();
    }

    public void RemoveElectron()
    {
        if (GetElectronCount() <= 2)
        {
            Transform parent = GetChildWithName("Inner Ring");
            List<GameObject> electronList = new List<GameObject>();
            foreach (Transform child in parent)
            {
                electronList.Add(child.gameObject);
            }
            GameObject e_t_remove = electronList[0];
            electronList.RemoveAt(0);
            RemoveFromNeighbours(e_t_remove, electronList);
            this.Electrons--;
        }
        else
        {
            Transform parent = GetChildWithName("Outer Ring");
            List<GameObject> electronList = new List<GameObject>();
            foreach (Transform child in parent)
            {
                electronList.Add(child.gameObject);
            }
            GameObject e_t_remove = electronList[0];
            electronList.RemoveAt(0);
            RemoveFromNeighbours(e_t_remove, electronList);

            this.Electrons--;
        }
        UpdateStructure();
    }

	void RemoveAll(){

	}
		

    public void AddProton()
    {
        Debug.Log("Added proton");
        this.Protons++;
        GameObject Temp = Instantiate(g_proton);

        Temp.transform.SetParent(cloud_core);
        if (GetProtonCount() <= 10)
        {
            Temp.transform.SetParent(cloud_core);
            Temp.transform.localPosition = Vector3.zero;
            Temp.GetComponent<SpringJoint>().connectedBody = cloud_core.GetComponent<Rigidbody>();
        }
        else
        {
            this.Protons--;
            Destroy(Temp);
        }

        UpdateStructure();
		ShootCannon ();
    }

    public void AddNeutron()
    {
        Debug.Log("Added neutron");
        this.Neutrons++;
        GameObject Temp = Instantiate(g_neutron);

        if (GetNeutronCount() <= 10)
        {
            Temp.transform.SetParent(cloud_core);
            Temp.transform.localPosition = Vector3.zero;
            Temp.GetComponent<SpringJoint>().connectedBody = cloud_core.GetComponent<Rigidbody>();
        }
        else
        {
            this.Neutrons--;
            Destroy(Temp);
        }

        UpdateStructure();
		ShootCannon ();
    }

    public void AddElectron()
    {
        Debug.Log("Added electron");
        this.Electrons++;
        GameObject Temp = Instantiate(g_electron);
        SpringJoint sj_Temp = Temp.GetComponent<SpringJoint>();
        if (GetElectronCount() <= 2)
        {
            Temp.transform.SetParent(GetChildWithName("Inner Ring"));
            Temp.transform.localPosition = Vector3.zero;
            sj_Temp.connectedBody = cloud_core.GetComponent<Rigidbody>();
            sj_Temp.maxDistance = 1.5f;
            sj_Temp.minDistance = 1.5f;
            if (GetElectronCount() == 2)
            {
                Transform Parent = GetChildWithName("Inner Ring");
                List<GameObject> go_list = new List<GameObject>();
                foreach(Transform child in Parent)
                {
                    go_list.Add(child.gameObject);
                }

                for (int i = 0; i<go_list.Count; i++)
                {
                    SpringJoint sj_child = Parent.GetChild(i).gameObject.AddComponent<SpringJoint>();
                    sj_child.minDistance = 5f;
                    sj_child.maxDistance = 5f;
                    if (i == go_list.Count - 1)
                    {
                        sj_child.connectedBody = Parent.GetChild(0).GetComponent<Rigidbody>();
                    }
                    else
                        sj_child.connectedBody = Parent.GetChild(i+1).GetComponent<Rigidbody>();
                }
            }
        }
        else if (GetElectronCount() <= 10)
        {

            Temp.transform.SetParent(GetChildWithName("Outer Ring"));
            Temp.transform.localPosition = Vector3.zero;
            sj_Temp.connectedBody = cloud_core.GetComponent<Rigidbody>();
            sj_Temp.maxDistance = 3f;
            sj_Temp.minDistance = 3f;
            if (GetElectronCount() >= 4)
            {
                Transform Parent = GetChildWithName("Outer Ring");
                List<GameObject> go_list = new List<GameObject>();
                foreach (Transform child in Parent)
                {
                    go_list.Add(child.gameObject);
                }
                AddToNeighbours(Temp, go_list);
                UpdateSprings(go_list, 1.5f);
            }
        }
        else
        {
            this.Electrons--;
            Destroy(Temp);
        }

        UpdateStructure();
		ShootCannon ();
    }

    void AddToNeighbours(GameObject electron, List<GameObject> listofelectrons)
    {
        for (int i = 0; i<listofelectrons.Count-1; i++)
        {
            float divCount = 1.5f;
            SpringJoint sj = electron.AddComponent<SpringJoint>();
            sj.connectedBody = listofelectrons[i].GetComponent<Rigidbody>();
            sj.spring = 20f;
            sj.damper = 10f;
            sj.maxDistance = 10f - (listofelectrons.Count / divCount);
            sj.minDistance = 10f - (listofelectrons.Count / divCount);

            sj = listofelectrons[i].AddComponent<SpringJoint>();
            sj.connectedBody = electron.GetComponent<Rigidbody>();
            sj.spring = 20f;
            sj.damper = 10f;
            sj.maxDistance = 10f - (listofelectrons.Count / divCount);
            sj.minDistance = 10f - (listofelectrons.Count / divCount);
        }
    }

    void UpdateSprings(List<GameObject> list, float divcount)
    {
        for (int i = 0; i < list.Count; i++)
        {
            foreach (SpringJoint sj in list[i].GetComponents<SpringJoint>())
            {
                if (sj.maxDistance > 3f)
                {
                    sj.maxDistance = 10f - (list.Count / divcount);
                    sj.minDistance = sj.maxDistance;
                }
            }
        }
    }

    void RemoveFromNeighbours(GameObject electron, List<GameObject> listofelectrons)
    {
        for (int i = 0; i < listofelectrons.Count; i++)
        {
            foreach(SpringJoint sj in listofelectrons[i].GetComponents<SpringJoint>())
            {
                if (sj.connectedBody == electron.GetComponent<Rigidbody>())
                {
                    Destroy(sj);
                }
            }
        }
        Destroy(electron);
        UpdateSprings(listofelectrons, 1.5f);
    }

    int GetElectronCount()
    {
        return this.Electrons;
    }

    int GetNeutronCount()
    {
        return this.Neutrons;
    }

    int GetProtonCount()
    {
        return this.Protons;
    }

    void RotateRings()
    {

    }
    
    void RotateCore()
    {
        cloud_core.transform.Rotate(Time.deltaTime*2, Time.deltaTime, 0, Space.World);
    }

    void GetRings()
    {
        foreach (Transform child in transform)
        {
            if (child.name.Contains("Ring"))
            {
                RingList.Add(child);
            }
        }
    }

    Transform GetChildWithName(string name)
    {
        foreach (Transform child in transform)
        {
            if (child.name.Contains(name))
            {
                return child;
            }
        }
        return null;
    }

    void UpdateStructure()
    {
        GetAtomInfo();
        if (GetNeutronCount() > GetProtonCount())
        {
            //UNSTABLE
            AtomInfoText.text += "\nUnstable!";
            Radioactive.SetActive(true);
        }
        else
        {
            Radioactive.SetActive(false);
        }

        if (GetProtonCount() <= 0)
        {
            AtomInfoText.text = "";
        }
    }

    void GetAtomInfo()
    {
        //if (GetNeutronCount() >= GetProtonCount())
        //{
            switch (GetProtonCount())
            {
                case 1:
                    AtomInfoText.text = "Hydrogen";
                    break;
                case 2:
                    AtomInfoText.text = "Helium";
                    break;
                case 3:
                    AtomInfoText.text = "Lithium";
                    break;
                case 4:
                    AtomInfoText.text = "Beryllium";
                    break;
                case 5:
                    AtomInfoText.text = "Boron";
                    break;
                case 6:
                    AtomInfoText.text = "Carbon";
                    break;
                case 7:
                    AtomInfoText.text = "Nitrogen";
                    break;
                case 8:
                    AtomInfoText.text = "Oxygen";
                    break;
                case 9:
                    AtomInfoText.text = "Fluorine";
                    break;
                case 10:
                    AtomInfoText.text = "Neon";
                    break;
                case 11:
                    AtomInfoText.text = "Sodium";
                    break;
            }
            if (GetElectronCount() > GetProtonCount())
                AtomInfoText.text += " -Ion";
            else if (GetElectronCount() < GetProtonCount())
                AtomInfoText.text += " +Ion";
            //AtomInfoText.text += string.Format("\nP:{0} | N:{1} | E:{2}", GetProtonCount(), GetNeutronCount(), GetElectronCount());
		AtomInfoText.text += string.Format("\nN:{1} | E:{2} | P:{0}", GetProtonCount(), GetNeutronCount(), GetElectronCount());
        //}
    }
}
