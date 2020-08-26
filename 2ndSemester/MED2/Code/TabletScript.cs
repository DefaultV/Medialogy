using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class TabletScript : MonoBehaviour {

	// Use this for initialization
	void Start () {
		
	}
    public GameObject Camera;
	// Update is called once per frame
	void Update () {
        transform.LookAt(2* transform.position - Camera.transform.position);
	}
}
