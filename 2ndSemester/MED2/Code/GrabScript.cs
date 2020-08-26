using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class GrabScript : MonoBehaviour {

	public GameObject left_cont;
	public GameObject right_cont;

	public GameObject proton;
	public GameObject neutron;
	public GameObject electron;
	GameObject tmp = null;
	public int Atom;
	// Use this for initialization
	void Start () {
		
	}
	
	// Update is called once per frame
	void Update () {

	}

	bool chosen = false;

	/*void Range(){
		if (Atom != null) {

			if (Vector3.Distance (transform.position, left_cont.transform.position) <= 1f 
				|| Vector3.Distance (transform.position, right_cont.transform.position <= 1f)){

				switch(Atom){
				case 1:
						tmp = Instantiate (proton);
						chosen = true;
						break;
					case 2:
						tmp = Instantiate (neutron);
						chosen = true;
						break;
					case 3:
						tmp = Instantiate (electron);
						chosen = true;
						break;
					default:
						break;
				}
			}
		}
	}

	int inRange(){
		if (Vector3.Distance (transform.position, left_cont.transform.position) <= 1f) {
			return 0;
		}
		if (Vector3.Distance (transform.position, right_cont.transform.position) <= 1f) {
			return 1;
		}
	}*/

	void ParentAtom(GameObject atom, GameObject parent){
		atom.transform.SetParent (parent.transform);
		atom.transform.localPosition = Vector3.zero;
	}
}
