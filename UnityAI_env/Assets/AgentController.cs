using UnityEngine;
using System.Collections;

public class AgentController : MonoBehaviour {

	// Use this for initialization
	void Start () {
		GetComponent<Rigidbody>().centerOfMass = new Vector3(0, 0, 1);
	}

	// speedを制御する
	public float speed = 10;	
	// Update is called once per frame
	void Update () {

		float x =  Input.GetAxis("Horizontal");
		float z = Input.GetAxis("Vertical");

		Rigidbody rigidbody = GetComponent<Rigidbody>();

		// xとyにspeedを掛ける
		rigidbody.AddForce(x * speed, 0, z * speed);
	}
}
