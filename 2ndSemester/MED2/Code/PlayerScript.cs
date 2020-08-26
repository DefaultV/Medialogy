using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.XR;

public class PlayerScript : MonoBehaviour {

	public SteamVR_TrackedController device;
	public string[] Inp;
	void Start () {
        player = GameObject.Find("PlayerSubstitude");
        atom = GameObject.Find("InteractiveAtom").GetComponent<AtomScript>();
		Inp = UnityEngine.Input.GetJoystickNames();
		lefthand = GetComponent<SteamVR_ControllerManager> ().left;
		righthand = GetComponent<SteamVR_ControllerManager> ().right;

        //Cursor.lockState = CursorLockMode.Locked;
	}
    public float distance = 50f;
    public GameObject Proton;
    public GameObject Neutron;
    public GameObject Electron;
    private GameObject player;

    public GameObject lefthand;
    public GameObject righthand;

    public GameObject ProtonPrefab_Bowl;
    public GameObject NeutronPrefab_Bowl;
    public GameObject ElectronPrefab_Bowl;
	public GameObject ResetButton;

	public AudioClip reset;
	public AudioClip shoot;
	public AudioClip pickup;

    bool chosenPart = false;
    bool Grab = false;

    AtomScript atom;
    GameObject tmp = null;
	GameObject handToparent = null;
    int switchPart = 0;

    void Update () {
		if (tmp != null && handToparent != null)
		{
			Debug.Log ("placing");
			Debug.Log (handToparent.transform.position);
			Debug.Log (tmp.transform.position);
			tmp.transform.position = handToparent.transform.position;
		}

		Debug.Log (lefthand.GetComponent<SteamVR_TrackedController>().triggerPressed);
		Debug.Log (righthand.GetComponent<SteamVR_TrackedController>().triggerPressed);

		if (lefthand.GetComponent<SteamVR_TrackedController>().triggerPressed || righthand.GetComponent<SteamVR_TrackedController>().triggerPressed) {
			Debug.Log ("Grabbing");
			SetGrab (true);
		}
        else
            SetGrab(false);

        if (Grabbing())
        {
            if (!chosenPart)
            {
				//Debug.Log (GetDistanceFromHands ());
				//Debug.Log (Vector3.Distance (lefthand.transform.position, ProtonPrefab_Bowl.transform.position));
                switch (GetDistanceFromHands())
                {
				case 1:
					tmp = Instantiate (Proton);
					handToparent = lefthand;
					switchPart = 1;
					GameObject.Find ("Jukebox").GetComponent<AudioSource> ().PlayOneShot (pickup);
                        break;
                    case 2:
                        tmp = Instantiate(Neutron);
					handToparent = lefthand;
                        switchPart = 2;
					GameObject.Find ("Jukebox").GetComponent<AudioSource> ().PlayOneShot (pickup);
                        break;
                    case 3:
                        tmp = Instantiate(Electron);
					handToparent = lefthand;
                        switchPart = 3;
					GameObject.Find ("Jukebox").GetComponent<AudioSource> ().PlayOneShot (pickup);
                        break;
				case 4:
					tmp = Instantiate (Proton);
					handToparent = righthand;
					switchPart = 1;
					GameObject.Find ("Jukebox").GetComponent<AudioSource> ().PlayOneShot (pickup);
                        break;
				case 5:
					tmp = Instantiate (Neutron);
					handToparent = righthand;
					switchPart = 2;
					GameObject.Find ("Jukebox").GetComponent<AudioSource> ().PlayOneShot (pickup);
						break;
				case 6:
					tmp = Instantiate (Electron);
					handToparent = righthand;
					switchPart = 3;
					GameObject.Find ("Jukebox").GetComponent<AudioSource> ().PlayOneShot (pickup);
						break;
                    default:
                        tmp = null;
                        break;
                }
                if (tmp == null)
                    return;
                chosenPart = true;
            }
        }

        if (tmp != null && !Grabbing())
        {
            float x = tmp.transform.position.x;
            float y = tmp.transform.position.y;
			Transform tube = GameObject.FindGameObjectWithTag("Tube").transform;
			if (Vector3.Distance (tmp.transform.position, tube.position) <= 2f) {
				GameObject.Find ("Jukebox").GetComponent<AudioSource> ().PlayOneShot (shoot);
				Destroy (tmp);
				chosenPart = false;
				switch (switchPart) {
				case 1:
					atom.AddProton ();
					switchPart = 0;
					break;
				case 2:
					atom.AddNeutron ();
					switchPart = 0;
					break;
				case 3:
					atom.AddElectron ();
					switchPart = 0;
					break;
				}
			} else {
				Destroy (tmp);
				chosenPart = false;
				handToparent = null;
			}
        }
    }

    bool Grabbing()
    {
            return this.Grab;
    }

    void SetGrab(bool state)
    {
        this.Grab = state;
    }

    int GetDistanceFromHands()
    {
        if (Vector3.Distance(lefthand.transform.position, ProtonPrefab_Bowl.transform.position) <= 2f)
        {
            return 1;
        }
        if (Vector3.Distance(lefthand.transform.position, NeutronPrefab_Bowl.transform.position) <= 2f)
        {
            return 2;
        }
        if (Vector3.Distance(lefthand.transform.position, ElectronPrefab_Bowl.transform.position) <= 2f)
        {
            return 3;
        }

		if (Vector3.Distance (righthand.transform.position, ProtonPrefab_Bowl.transform.position) <= 2f) {
			return 4;
		}
		if (Vector3.Distance (righthand.transform.position, NeutronPrefab_Bowl.transform.position) <= 2f) {
			return 5;
		}
		if (Vector3.Distance (righthand.transform.position, ElectronPrefab_Bowl.transform.position) <= 2f) {
			return 6;
		}
        return 0;
    }
}
