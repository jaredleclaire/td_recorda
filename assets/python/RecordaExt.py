"""
Extension classes enhance TouchDesigner components with python. An
extension is accessed via ext.ExtensionClassName from any operator
within the extended component. If the extension is promoted via its
Promote Extension parameter, all its attributes with capitalized names
can be accessed externally, e.g. op('yourComp').PromotedFunction().

Help: search "Extensions" in wiki
"""

from TDStoreTools import StorageManager
import TDFunctions as TDF

class recorda:
	"""
	recorda description
	"""
	def __init__(self, ownerComp):
		# The component to which this extension is attached
		self.ownerComp = ownerComp

		# properties
		TDF.createProperty(self, 'MyProperty', value=0, dependable=True,
						   readOnly=False)

		# attributes:
		self.a = 0 # attribute
		self.B = 1 # promoted attribute

		# stored items (persistent across saves and re-initialization):
		storedItems = [
			# Only 'name' is required...
			{'name': 'StoredProperty', 'default': None, 'readOnly': False,
			 						'property': True, 'dependable': True},
		]
		# Uncomment the line below to store StoredProperty. To clear stored
		# 	items, use the Storage section of the Component Editor
		
		# self.stored = StorageManager(self, ownerComp, storedItems)

	def RecordStart(self):
		
		op('math_pulse').par.gain = 1
		
		#debug()
		
	def RecordStop(self):
		
		op('math_pulse').par.gain = 0
		me.parent().TakePlus()
		
		#debug()
	
	def TakePlus(self):

		take = int( op.Recorda.par.Take ) + 1
		me.parent().par.Take = take
		
		#debug()
		
	def TakeMinus(self):

		take = int( op.Recorda.par.Take ) - 1
		me.parent().par.Take = take
		
		#debug()
		
	def TakeReset(self):

		me.parent().par.Take = 1
		
		#debug()
		
	def Snapshot(self):
		
		savePath = str(op.Recorda.par.Recordlocation) + '/_snapshots'
		date = op('null_dateprepend')[0,0]
		description = op.Recorda.par.Description
		angle = op.Recorda.par.Angle
		time = str(int(op('null_tod')['hour'])) + str(int(op('null_tod')['min'])) + str(int(op('null_tod')['sec']))
	
		op('null_snapshot').save(savePath + '/' + description + '_' + angle + '_snapshot' + '_' + time + '.png')
		
		#debug()
	
	def PollInputDevices(self):

		#retrieve video input device list and create parMenu object
		VideoInputDevices = op('videodevout1').par.device.menuNames

		VideoInputDevices = TDF.parMenu(VideoInputDevices)

		op.Recorda.store('VideoInputDevices',VideoInputDevices)
		
		#retreive audio input device list and create parMenu object
		AudioInputDevices = op('audiodevin1').par.device.menuNames

		AudioInputDevices = TDF.parMenu(AudioInputDevices)

		op.Recorda.store('AudioInputDevices',AudioInputDevices)

		#print()

		#debug()
		return()
	
	def PollOutputDevices(self):

		#retreive video device list and create parMenu object	
		VideoOutputDevices = op('videodevout1').par.device.menuNames
		VideoOutputFormats = op('videodevout1').par.signalformat.menuNames

		VideoOutputDevices = TDF.parMenu(VideoOutputDevices)
		VideoOutputFormats = TDF.parMenu(VideoOutputFormats)

		op.Recorda.store('VideoOutputDevices',VideoOutputDevices)
		op.Recorda.store('VideoOutputFormats',VideoOutputFormats)

		debug()
		return()
	
	def Legalize(self, mode):

		if mode == 'bypass':
			op('ocio_legalize').par.usefiletransform = False
			print('Bypass configured')
			pass

		elif mode == 'fulltolegal':
			op('ocio_legalize').par.usefiletransform = True
			op('ocio_legalize').par.filedirection = 1
			print('Full to Legal configured')
			pass

		elif mode == 'legaltofull':
			op('ocio_legalize').par.usefiletransform = True
			op('ocio_legalize').par.filedirection = 0
			print('Legal to Full configured')
			pass

		else:
			pass

		debug()